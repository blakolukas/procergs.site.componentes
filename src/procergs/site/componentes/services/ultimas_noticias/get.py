from plone.restapi.interfaces import ISerializeToJsonSummary
from plone.restapi.services import Service
from zope.component import getMultiAdapter


class UltimasNoticiasGet(Service):
    """endpoint customizado para exibir ultimas noticias"""

    def reply(self):
        catalog = self.context.portal_catalog
        request = self.request

        query = {
            "portal_type": "News Item",
        }

        sort_on = ["effective"]

        indicador_manchete = request.form.get("manchete")
        if indicador_manchete is not None and indicador_manchete.lower() in [
            "true",
            "1",
        ]:
            sort_on = ["indicador_manchete", "effective"]

        indicador_destaque = request.form.get("destaque")
        if indicador_destaque is not None and indicador_destaque.lower() in [
            "true",
            "1",
        ]:
            sort_on = ["indicador_destaque", "effective"]

        itens = int(request.form.get("itens", 3))
        if itens < 2 or itens > 4:
            raise ValueError("O parâmetro 'itens' deve ser um número entre 2 e 4.")

        results = catalog(
            **query,
            sort_on=sort_on,
            sort_order="descending",
            sort_limit=int(itens),
        )

        brains = [
            getMultiAdapter((brain, request), ISerializeToJsonSummary)()
            for brain in results
        ]

        return {
            "@id": self.context.absolute_url() + "/@ultimas_noticias",
            "items": brains,
            "items_total": len(brains),
        }
