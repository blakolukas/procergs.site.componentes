from plone import api
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from procergs.sitedemo import PACKAGE_NAME

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
    }


@pytest.fixture
def contents(portal, secretaria_payload, local_payload):
    with api.env.adopt_roles(["Manager"]):
        secretaria = api.content.create(container=portal, **secretaria_payload)
        local = api.content.create(container=secretaria, **local_payload)
        return [secretaria, local]


class TestVocabLocais:
    name = f"{PACKAGE_NAME}.vocabulary.locais"

    @pytest.fixture(autouse=True)
    def _vocab(self, get_vocabulary, contents):
        secretaria, local = contents
        self.vocab = get_vocabulary(self.name, secretaria)

    def test_vocabulary(self):
        assert self.vocab is not None
        assert isinstance(self.vocab, StaticCatalogVocabulary)

    @pytest.mark.parametrize(
        "title",
        [
            "Casa Civil",
        ],
    )
    def test_results(self, title):
        assert title in [brain.Title for brain in self.vocab.brains]
