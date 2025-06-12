from plone.dexterity.content import Container
from plone.supermodel import model
from procergs.site.componentes import _
from zope import schema
from zope.interface import implementer


class ICustomNewsItem(model.Schema):
    pattern_news = schema.Choice(
        title=_("Padrão"),
        description=_("Selecione o padrão de exibição do conteúdo."),
        vocabulary="procergs.site.componentes.vocabulary.patternNoticias",
        required=True,
        default="padrao1",
    )
    
    indicador_destaque = schema.Bool(
        title=_("Destaque"),
        description=_("Indica se o conteúdo é um destaque"),
        required=False,
        default=False,
    )

    indicador_manchete = schema.Bool(
        title=_("Manchete"),
        description=_("Indica se o conteúdo é uma manchete"),
        required=False,
        default=False,
    )


@implementer(ICustomNewsItem)
class CustomNewsItem(Container):
    """Customização do tipo de conteúdo Notícia"""

    pass
