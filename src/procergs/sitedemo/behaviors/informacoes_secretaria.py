from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IInformacoesSecretaria(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "secretaria",
        _("Informações Secretaria"),
        fields=[
            "local",
            "nome_secretaria_vinculada",
            "url_secretaria_vinculada",
        ],
    )

    local = RelationChoice(
        title="Local",
        description="Localização deste orgão",
        vocabulary="procergs.sitedemo.vocabulary.locais",
        required=False,
    )

    nome_secretaria_vinculada = schema.TextLine(
        title=_("Nome da Secretaria Vinculada"),
        description=_("Informe o nome da secretaria vinculada"),
        required=False,
    )

    url_secretaria_vinculada = schema.TextLine(
        title=_("URL da Secretaria Vinculada"),
        description=_("Informe a URL da secretaria vinculada"),
        required=False,
    )
