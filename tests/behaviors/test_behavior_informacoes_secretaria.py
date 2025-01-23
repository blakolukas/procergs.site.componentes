from procergs.sitedemo import PACKAGE_NAME

import pytest


@pytest.fixture
def payload() -> dict:
    return {
        "local": {
            "logradouro": "Praça Marechal Deodoro, s/n",
            "complemento": "Centro Histórico",
            "municipio": "Porto Alegre",
            "estado": "RS",
            "cep": "90010-905",
        },
        "nome_secretaria_vinculada": "Secretaria da Fazenda",
        "url_secretaria_vinculada": "https://www.fazenda.rs.gov.br",
    }


class TestBehaviorContato:
    name: str = f"{PACKAGE_NAME}.behavior.informacoes_secretaria"

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
