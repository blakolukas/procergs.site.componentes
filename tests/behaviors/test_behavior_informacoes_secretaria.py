from plone import api
from procergs.site.componentes import PACKAGE_NAME
from procergs.site.componentes.content.local import Local

import pytest


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
        "logradouro": "Rua do governo",
    }


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
        "email": "gabinete@casacivil.rs.gov.br",
        "telefone": "(51) 3210.4193",
        "nome_secretaria_vinculada": "Secretaria da Fazenda",
        "url_secretaria_vinculada": "https://www.fazenda.rs.gov.br",
    }


@pytest.fixture
def informacoes_secretaria_payload() -> dict:
    """Return a payload from behavior informacoes_secretaria."""
    return {
        "nome_secretaria_vinculada": "Secretaria da Fazenda",
        "url_secretaria_vinculada": "https://www.fazenda.rs.gov.br",
    }


@pytest.fixture
def contents(portal, secretaria_payload, local_payload):
    with api.env.adopt_roles(["Manager"]):
        secretaria = api.content.create(container=portal, **secretaria_payload)
        local = api.content.create(container=secretaria, **local_payload)
        return [secretaria, local]


class TestBehaviorInformacoesSecretaria:
    name: str = f"{PACKAGE_NAME}.behavior.informacoes_secretaria"

    @pytest.fixture(autouse=True)
    def _setup(self, portal_factory, dummy_type_schema):
        self.portal = portal_factory(behavior=self.name)
        self.schema = dummy_type_schema()

    def test_behavior_schema(self, informacoes_secretaria_payload):
        for key in informacoes_secretaria_payload:
            assert key in self.schema["properties"]

    def test_secretaria_has_child_local(self, contents):
        secretaria, local = contents
        assert isinstance(secretaria["casacivil"], Local)

    # @TODO: teste para ver se o local é do tipo dicionário
    # def test_behavior_data(self, informacoes_secretaria_payload, create_dummy_content, local_payload):
    #     response_local = create_dummy_content(local_payload)
    #     assert response_local.status_code == 201

    #     informacoes_secretaria_payload["local"] = {
    #         "@id": response_local.json().get("UID")
    #     }

    #     # É do tipo local, mas da error no backend
    #     #{'message': 'Constraint not satisfied', 'field': 'local', 'error': 'ValidationError'}
    #     response = create_dummy_content(informacoes_secretaria_payload)
    #     assert response.status_code == 201
