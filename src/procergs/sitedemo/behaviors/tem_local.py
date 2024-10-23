from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from z3c.relationfield.schema import RelationChoice
from zope.interface import provider


@provider(IFormFieldProvider)
class IInformacoesSecretaria(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "local",
        _("Localização"),
        fields=[
            "local",
        ],
    )

    local = RelationChoice(
        title="Local",
        description="Localização deste orgão",
        vocabulary="portal.governo.vocabulary.locais",
        required=False,
    )
