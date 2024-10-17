from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from plone.restapi.testing import RelativeSession
from zope.component.hooks import setSite

import pytest
import transaction


@pytest.fixture()
def request_factory(portal):
    def factory():
        url = portal.absolute_url()
        api_session = RelativeSession(url)
        api_session.headers.update({"Accept": "application/json"})
        return api_session

    return factory


@pytest.fixture()
def anon_request(request_factory):
    return request_factory()


@pytest.fixture()
def manager_request(request_factory):
    request = request_factory()
    request.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    yield request
    request.auth = ()


@pytest.fixture
def portal(functional):
    return functional["portal"]


@pytest.fixture
def portal_integration(integration):
    return integration["portal"]


@pytest.fixture
def portal_factory(functional):
    def func(behavior: str):
        portal = functional["portal"]
        setRoles(portal, TEST_USER_ID, ["Manager"])
        fti = DexterityFTI("DummyType")
        fti.behaviors = (behavior,)
        portal.portal_types._setObject("DummyType", fti)
        setSite(portal)
        transaction.commit()
        return portal

    return func


@pytest.fixture
def dummy_type_schema(manager_request):
    def func():
        url = "/@types/DummyType"
        response = manager_request.get(url)
        data = response.json()
        return data

    return func


@pytest.fixture
def create_dummy_content(manager_request):
    def func(payload: dict):
        payload["@type"] = "DummyType"
        response = manager_request.post("/", json=payload)
        return response

    return func
