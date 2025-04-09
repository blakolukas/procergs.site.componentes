from plone.autoform.interfaces import IFormFieldProvider
from plone.base.interfaces import IPloneSiteRoot
from plone.dexterity.utils import iterSchemata
from plone.restapi.interfaces import IFieldSerializer
from plone.restapi.serializer.dxfields import DefaultFieldSerializer
from procergs.site.componentes.interfaces import IBrowserLayer
from z3c.relationfield.schema import RelationChoice
from zope.component import adapter
from zope.interface import implementer


@implementer(IFieldSerializer)
@adapter(RelationChoice, IPloneSiteRoot, IBrowserLayer)
class LocalChoiceSerializer(DefaultFieldSerializer):
    def __call__(self, *args, **kwargs):
        result = super().__call__(*args, **kwargs)

        value = self.field.get(self.context)
        if value:
            target = value.to_object
            serialized_target = {}
            for schema in iterSchemata(target):
                for name, field in schema.namesAndDescriptions(all=True):
                    if IFormFieldProvider.providedBy(schema) and name not in [
                        "blocks",
                        "blocks_layout",
                    ]:
                        serialized_target[name] = field.get(target)

            result["data"] = serialized_target

        return result
