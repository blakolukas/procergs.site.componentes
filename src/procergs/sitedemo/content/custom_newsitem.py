from plone.dexterity.content import Container
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import implementer


class ICustomNewsItem(model.Schema):
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
