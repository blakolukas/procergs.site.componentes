from plone import api
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.services import Service
from z3c.relationfield.relation import RelationValue
from zope.component import getMultiAdapter
from zope.component import queryUtility
from zope.intid.interfaces import IIntIds


class LocalPrincipalGet(Service):
    """Retorna local principal."""

    def serializa(self, content) -> dict:
        """Serializa um objeto como dicionário."""
        serializador = getMultiAdapter((content, self.request), ISerializeToJson)
        return serializador()

    def reply(self) -> dict:
        plone_site = api.portal.get()

        local_relation = getattr(plone_site, "local", None)

        if not local_relation or not isinstance(local_relation, RelationValue):
            # If there is no relation set or it is not a valid relation, return empty result
            return {"@id": f"{self.context.absolute_url()}", "items": []}

        # Resolve the relation to get the referenced 'Local' content
        intids = queryUtility(IIntIds)
        if intids is None:
            return {"@id": f"{self.context.absolute_url()}", "items": []}

        local_obj = local_relation.to_object if local_relation else None

        # If the relation is valid and the content exists
        if local_obj is not None and local_obj.portal_type == "Local":
            # Serialize the 'Local' content as a summary
            item = self.serializa(local_obj)
            return {"@id": f"{self.context.absolute_url()}", "items": [item]}

        # If no valid 'Local' content found, return empty result
        return {"@id": f"{self.context.absolute_url()}", "items": []}


class ListaGet(Service):
    """Retorna local principal."""

    def serializa_como_sumario(self, content) -> dict:
        """Serializa um objeto como dicionário."""
        serializador = getMultiAdapter((content, self.request), ISerializeToJson)
        return serializador()

    def reply(self) -> dict:
        """Resposta ao endpoint de secretarias."""
        items = []

        brains = api.content.find(
            portal_type="Local", sort_on="sortable_title", sort_order="ascending"
        )
        for brain in brains:
            content = brain.getObject()
            item = self.serializa_como_sumario(content)
            items.append(item)

        # Retornar resultado
        return {"@id": f"{self.context.absolute_url()}", "items": items}
