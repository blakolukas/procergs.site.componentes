from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ILocal(model.Schema):
    """Dados do local"""


@implementer(ILocal)
class Local(Container):
    """Um Local"""
