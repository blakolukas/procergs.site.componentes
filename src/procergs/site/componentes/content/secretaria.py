from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer


class ISecretaria(model.Schema):
    """Dados da secretaria"""


@implementer(ISecretaria)
class Secretaria(Container):
    """Uma secretaria de governo."""
