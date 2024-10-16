from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IInformacoesSecretaria(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "secretaria",
        _("Informações Secretaria"),
        fields=[
            "nome_secretaria_vinculada",
            "url_secretaria_vinculada",
        ],
    )

    nome_secretaria_vinculada = schema.TextLine(
        title=_("Gnome da Secretaria Vinculada"),
        description=_("Informe o gnome da secretaria vinculada"),
        required=False,
    )

    url_secretaria_vinculada = schema.TextLine(
        title=_("URL da Secretaria Vinculada"),
        description=_("Informe a URL da secretaria vinculada"),
        required=False,
    )
