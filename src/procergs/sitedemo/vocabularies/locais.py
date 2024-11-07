from plone import api
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def vocab_locais(context=None):
    """Vocabulário de locais"""
    if context is None:
        context = api.portal.get()
    folder_path = "/".join(context.getPhysicalPath())
    return StaticCatalogVocabulary(
        {
            "path": {"query": folder_path, "depth": 2},
            "portal_type": ["Local"],
            "sort_on": "sortable_title",
        }
    )
