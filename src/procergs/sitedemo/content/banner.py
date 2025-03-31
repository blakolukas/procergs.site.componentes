from plone.dexterity.content import Container
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import implementer


class IBanner(model.Schema):
    """Dados da banner"""

    url = schema.TextLine(
        title=_("Link"),
        description=_("URL destino"),
        required=False,
        default=False,
    )


@implementer(IBanner)
class Banner(Container):
    """Um banner"""
