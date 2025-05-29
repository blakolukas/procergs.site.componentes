from plone import api

import logging


default_profile = "profile-procergs.site.componentes:default"
logger = logging.getLogger(__name__)


def update_indexes(setup_tool):
    # Atualiza indices
    setup_tool.runImportStepFromProfile(default_profile, "catalog")
    # Reindexa notícias
    for brain in api.content.find(portal_type=["News Item"]):
        obj = brain.getObject()
        obj.reindexObject()
        logger.info(f"{obj.id} reindexed.")
