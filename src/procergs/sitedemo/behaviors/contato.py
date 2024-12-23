from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from procergs.sitedemo import _
from procergs.sitedemo.utils import validadores
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IContato(model.Schema):
    """Provê campos de contato."""

    model.fieldset(
        "contato",
        _("Contato"),
        fields=[
            "email",
            "fax",
            "telefone_fax",
            "tel_comercial",
            "tel_celular",
            "voip",
            "skype",
            "whatsapp",
            "url",
            "horarios",
            "link_whatsapp",
            "telefones",
        ],
    )

    email = Email(
        title=_("Email"),
        required=False,
    )
    fax = schema.TextLine(
        title="FAX",
        required=False,
    )
    telefone_fax = schema.TextLine(
        title="TEL/FAX",
        required=False,
    )
    tel_comercial = schema.TextLine(
        title="Telefone Comercial",
        required=False,
    )
    tel_celular = schema.TextLine(
        title="Telefone Celular",
        required=False,
    )
    voip = schema.TextLine(
        title="VOIP",
        required=False,
    )
    skype = schema.TextLine(
        title="Skype",
        required=False,
    )
    whatsapp = schema.TextLine(
        title="WhatsApp",
        required=False,
    )

    directives.widget(
        "url",
        frontendOptions={
            "format": "url",
        },
    )
    url = schema.TextLine(
        title="URL",
        required=False,
    )
    horarios = schema.TextLine(
        title="Horários de Atendimento",
        required=False,
    )
    link_whatsapp = schema.TextLine(
        title="Link WhatsApp",
        required=False,
    )

    directives.widget(
        "telefones",
        frontendOptions={
            "widget": "lista_telefones",
        },
    )
    telefones = schema.List(
        title="Telephone Numbers",
        value_type=schema.TextLine(
            title="Telefone",
            constraint=validadores.is_valid_telefone,
        ),
        required=False,
        min_length=1,
        max_length=5,
    )
