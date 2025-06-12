# src/procergs/site/componentes/vocabularies.py
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory


@provider(IVocabularyFactory)
def pattern_noticias(context) -> SimpleVocabulary:
    return SimpleVocabulary([
        SimpleTerm("padrao1",     title=("Padrão 1")),
        SimpleTerm("padrao2",  title=("Padrão 2")),
        SimpleTerm("padrao3",     title=("Padrão 3")),
    ])
