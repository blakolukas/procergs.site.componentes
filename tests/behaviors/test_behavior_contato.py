from procergs.sitedemo import PACKAGE_NAME

import pytest


@pytest.fixture
def payload() -> dict:
    return {
        "telefones": ["51999528312"],
        "fax": "51999528312",
        "telefone_fax": "51999528312",
        "tel_comercial": "51999528312",
        "tel_celular": "51999528312",
        "voip": "51999528312",
        "skype": "51999528312",
        "whatsapp": "51999528312",
        "email": "foo@procergs.rs.gov.br",
        "url": "http://rs.gov.br",
        "horarios": "das 10h às 15h",
        "link_whatsapp": "51999528312",
    }


class TestBehaviorContato:
    name: str = f"{PACKAGE_NAME}.behavior.contato"

    @pytest.fixture(autouse=True)
    def _setup(self, portal_factory, dummy_type_schema):
        self.portal = portal_factory(behavior=self.name)
        self.schema = dummy_type_schema()

    def test_behavior_schema(self, payload):
        for key in payload:
            assert key in self.schema["properties"]

    def test_behavior_data(self, payload, create_dummy_content):
        response = create_dummy_content(payload)
        assert response.status_code == 201
