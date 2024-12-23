from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IExtras(model.Schema):
    """Provê campos extras vindos do Matriz Framework."""

    model.fieldset(
        "extras",
        _("Informações Extras"),
        fields=[
            "subtitle",
            "observacao_interna",
            "matriz_id",
            "matriz_codigo_externo",
        ],
    )

    subtitle = schema.TextLine(title="Subtítulo", required=False, default="")

    observacao_interna = schema.TextLine(
        title="Observação Interna", required=False, default=""
    )

    matriz_id = schema.TextLine(title="Matriz - ID", required=False, default="")

    matriz_codigo_externo = schema.TextLine(
        title="Matriz - codigo externo", required=False, default=""
    )
