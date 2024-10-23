from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from procergs.sitedemo import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IEndereco(model.Schema):
    """Provê campos de endereço."""

    model.fieldset(
        "local",
        _("Local"),
        fields=[
            "logradouro",
            "numero",
            "complemento",
            "bairro",
            "municipio",
            "municipio_id",
            "estado",
            "pais",
            "cep",
            "coordenadas",
        ],
    )
    logradouro = schema.TextLine(
        title=_("Logradouro"),
        required=False,
        default="",
    )
    numero = schema.TextLine(
        title=_("Número"),
        required=False,
        default="",
    )
    complemento = schema.TextLine(
        title=_("Complemento"),
        description=_("Bloco, Apartamento, etc"),
        required=False,
        default="",
    )
    bairro = schema.TextLine(
        title=_("Bairro"),
        required=False,
        default="",
    )
    municipio = schema.TextLine(
        title=_("Municipio"),
        required=False,
        default="",
    )
    municipio_id = schema.TextLine(
        title=_("Municipio ID"),
        required=False,
        default="",
    )
    estado = schema.Choice(
        title=_("UF"),
        vocabulary="procergs.sitedemo.vocabulary.estados",
        required=False,
    )
    pais = schema.TextLine(
        title=_("Pais"),
        required=False,
        default="",
    )
    cep = schema.TextLine(
        title=_("CEP"),
        required=False,
        default="",
    )
    coordenadas = schema.TextLine(
        title=_("Coordenadas"),
        required=False,
        default="",
    )
