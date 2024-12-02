from pathlib import Path
from plone_manager import PloneManager

import json


def loadJsonFile(filename):
    with open(filename) as file:
        json_data = json.load(file)
    return json_data


plone = PloneManager()
PASTA_ATUAL = Path(__file__).parent.resolve()

menu_institucional = loadJsonFile(PASTA_ATUAL / "institucional.json")
menu_comunic = loadJsonFile(PASTA_ATUAL / "comunicacao.json")
menu_projetos = loadJsonFile(PASTA_ATUAL / "projetos.json")

plone.cadastraConteudos(menu_institucional)
plone.cadastraConteudos(menu_comunic)
plone.cadastraConteudos(menu_projetos)
