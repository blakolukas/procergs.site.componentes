from pathlib import Path
from plone_manager import PloneManager

import json


def loadJsonFile(filename):
    with open(filename) as file:
        json_data = json.load(file)
    return json_data


plone = PloneManager()
PASTA_ATUAL = Path(__file__).parent.resolve()

menu_comunic = loadJsonFile(PASTA_ATUAL / "sustentare/comunicacao.json")
menu_servicos = loadJsonFile(PASTA_ATUAL / "sustentare/servicos.json")
menu_programa = loadJsonFile(PASTA_ATUAL / "sustentare/o-programa.json")
banners = loadJsonFile(PASTA_ATUAL / "sustentare/banners.json")
home = loadJsonFile(PASTA_ATUAL / "sustentare/home.json")


# plone.cadastraConteudos(menu_comunic)
# plone.cadastraConteudos(menu_servicos)
# plone.cadastraConteudos(menu_programa)
plone.cadastraConteudos(banners)
plone.atualizaCapa(home)
