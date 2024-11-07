from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IExtras(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "extras",
        _("Informações Extras"),
        fields=[
            "subtitulo",
            "indicador_destaque",
            "indicador_manchete",
            "credito",
            "observacao_interna",
            "matriz_id",
            "matriz_codigo_externo",
        ],
    )

    subtitulo = schema.TextLine(title="Subtítulo", required=False, default="")

    indicador_destaque = schema.Bool(title="Destaque", required=False, default=False)

    indicador_manchete = schema.Bool(title="Manchete", required=False, default=False)

    credito = schema.TextLine(title="Crédito", required=False, default="")

    observacao_interna = schema.TextLine(
        title="Observação Interna", required=False, default=""
    )

    matriz_id = schema.TextLine(title="Matriz - ID", required=False, default="")

    matriz_codigo_externo = schema.TextLine(
        title="Matriz - codigo externo", required=False, default=""
    )
