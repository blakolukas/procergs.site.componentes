from AccessControl import Unauthorized
from plone import api
from plone.dexterity.fti import DexterityFTI
from procergs.site.componentes.content.local import Local
from zope.component import createObject

import pytest


CONTENT_TYPE = "Local"


@pytest.fixture
def local_payload() -> dict:
    """Return a payload to create a new local."""
    return {
        "type": "Local",
        "id": "casacivil",
        "title": "Casa Civil",
        "description": (
            "A Casa Civil do Governo do Estado foi criada em janeiro de 1954,"
            "pelo então governador Ernesto Dornelles"
        ),
        "logradouro": "Rudo do governo",
    }


@pytest.fixture()
def content(portal, local_payload) -> Local:
    with api.env.adopt_roles(["Manager"]):
        content = api.content.create(container=portal, **local_payload)
    return content


class TestLocal:
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
        assert isinstance(obj, Local)

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
    def test_create(self, local_payload, role, allowed):
        with api.env.adopt_roles([role]):
            if allowed:
                content = api.content.create(container=self.portal, **local_payload)
                assert content.portal_type == CONTENT_TYPE
                assert isinstance(content, Local)
            else:
                with pytest.raises(Unauthorized):
                    api.content.create(container=self.portal, **local_payload)

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
                "procergs.site.componentes: Add Local", user=current_user, obj=content
            )
            assert can_add is allowed
