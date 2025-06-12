import json
import logging
from pathlib import Path
from typing import Dict, Tuple, Union

from zope.component import adapter
from zope.lifecycleevent.interfaces import IObjectAddedEvent, IObjectModifiedEvent

from procergs.site.componentes.content.custom_newsitem import ICustomNewsItem
from plone.restapi.behaviors import IBlocks

logger = logging.getLogger(__name__)
PASTA_ATUAL = Path(__file__).parent.resolve()
current_template = "padrao1" 


def load_json_file(path: Path) -> Dict:
    try:
        with path.open() as fp:
            return json.load(fp)
    except Exception as exc:
        logger.error("Falha lendo %s (%s)", path.name, exc)
        return {}


def build_template(template_id: str) -> Tuple[Dict, Dict]:
    json_path = PASTA_ATUAL / f"{template_id}.json"
    logger.info("Carregando template %s de %s", template_id, json_path)
    if not json_path.exists():
        logger.warning("Template %s inexistente; usando vazio", template_id)
        return {}, {"items": []}
    data = load_json_file(json_path)
    # garante que sempre haja uma lista no layout
    layout = data.get("blocks_layout", {})
    if "items" not in layout:
        layout = {"items": []}
    return data.get("blocks", {}), layout


def _normalize(value: Union[str, list, tuple, None]) -> str:
    """Converte Choice ou List para string única."""
    if not value:
        return "padrao1"
    if isinstance(value, (list, tuple)):
        return value[0] if value else "padrao1"
    return str(value)


def _get_template_id(context) -> str:
    raw = getattr(context, "select_pattern", None)
    return _normalize(raw)


def _apply_blocks(context, template_id: str):
    blocks, blocks_layout = build_template(template_id)
    behavior = IBlocks(context, None)
    if not behavior:
        logger.warning("%s sem comportamento Blocks; abortando", context.portal_type)
        return
    behavior.blocks = blocks
    behavior.blocks_layout = blocks_layout
    context._last_applied_pattern = template_id  # persiste
    context.reindexObject()


#SUBSCRIBERS

@adapter(ICustomNewsItem, IObjectAddedEvent)
def init_pattern_news(context, event):
    logger.info("Aplicando blocos de %s", context.id)
    template_id = _get_template_id(context)
    _apply_blocks(context, template_id)
    logger.info("Blocos aplicados (add) em %s [template %s]", context.id, template_id)


@adapter(ICustomNewsItem, IObjectModifiedEvent)
def update_pattern_news(context, event):
    global current_template 
    context_template = context.pattern_news
    logger.info("Atualizando blocos de %s", context_template)
    if context_template == current_template:
        return
    current_template = context_template
    _apply_blocks(context, current_template)
    logger.info("Blocos atualizados (mod) em %s [template %s]", context.id, context_template)
