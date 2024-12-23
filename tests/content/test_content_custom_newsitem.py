from plone import api
from plone.dexterity.fti import DexterityFTI
from procergs.sitedemo.content.local import Local
from zope.component import createObject

import pytest


CONTENT_TYPE = "Local"


@pytest.fixture
def local_payload() -> dict:
    """Return a payload to create a new custom news."""
    return {
        "type": "News Item",
        "id": "noticias",
        "title": "Noticias",
        "indicador_destaque": False,
        "indicador_machete": False,
    }


@pytest.fixture()
def content(portal, local_payload) -> Local:
    with api.env.adopt_roles(["Manager"]):
        content = api.content.create(container=portal, **local_payload)
    return content


class TestCustomNewsItem:
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
        ["procergs.sitedemo.behavior.extras"],
    )
    def test_has_behavior(self, get_behaviors, behavior):
        assert behavior in get_behaviors(CONTENT_TYPE)
