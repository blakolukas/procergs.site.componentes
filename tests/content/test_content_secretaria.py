from AccessControl import Unauthorized
from plone import api
from plone.dexterity.fti import DexterityFTI
from procergs.site.componentes.content.secretaria import Secretaria
from zope.component import createObject

import pytest


CONTENT_TYPE = "Secretaria"


@pytest.fixture
def secretaria_payload() -> dict:
    """Return a payload to create a new secretaria."""
    return {
        "type": "Secretaria",
        "id": "casacivil",
        "title": "Casa Civil",
        "description": (
            "A Casa Civil do Governo do Estado foi criada em janeiro de 1954,"
            "pelo então governador Ernesto Dornelles"
        ),
        "nome_secretaria_vinculada": "Governo",
        "url_secretaria_vinculada": "rs.gov.br",
    }


@pytest.fixture()
def content(portal, secretaria_payload) -> Secretaria:
    with api.env.adopt_roles(["Manager"]):
        content = api.content.create(container=portal, **secretaria_payload)
    return content


class TestSecretaria:
    @pytest.fixture(autouse=True)
    def _setup(self, get_fti, portal):
        self.fti = get_fti(CONTENT_TYPE)
        self.portal = portal

    def test_fti(self):
        assert isinstance(self.fti, DexterityFTI)

    def test_factory(self):
        factory = self.fti.factory
        obj = createObject(factory)
        assert obj is not None
        assert isinstance(obj, Secretaria)

    @pytest.mark.parametrize(
        "behavior",
        [
            "plone.basic",
            "plone.namefromtitle",
            "plone.shortname",
            "plone.excludefromnavigation",
            "plone.versioning",
            "plone.constraintypes",
            "volto.preview_image",
        ],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)

    @pytest.mark.parametrize(
        "role,allowed",
        [
            ["Manager", True],
            ["Site Administrator", True],
            ["Editor", False],
            ["Contributor", False],
        ],
    )
    def test_create(self, secretaria_payload, role, allowed):
        with api.env.adopt_roles([role]):
            if allowed:
                content = api.content.create(
                    container=self.portal, **secretaria_payload
                )
                assert content.portal_type == CONTENT_TYPE
                assert isinstance(content, Secretaria)
            else:
                with pytest.raises(Unauthorized):
                    api.content.create(container=self.portal, **secretaria_payload)

    @pytest.mark.parametrize(
        "role,allowed",
        [
            ["Manager", False],
            ["Site Administrator", False],
            ["Editor", False],
            ["Contributor", False],
        ],
    )
    def test_permission_inside_content(self, content, role, allowed):
        current_user = api.user.get_current()
        with api.env.adopt_roles([role]):
            can_add = api.user.has_permission(
                "procergs.site.componentes: Add Secretaria",
                user=current_user,
                obj=content,
            )
            assert can_add is allowed
