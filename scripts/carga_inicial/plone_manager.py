import logging
import requests


# Class responsável pelas interações com o Plone API
class PloneManager:
    def __init__(self):
        self.BASE_URL = "http://localhost:8080/Plone/++api++"
        self.USUARIO = "admin"
        self.SENHA = "admin"
        self.session = self.getAuthenticatedSession()
        self.logger = self.getLogger()

    def getAuthenticatedSession(self):
        session = requests.Session()
        headers = {"Accept": "application/json"}
        session.headers.update(headers)

        login_url = f"{self.BASE_URL}/@login"
        response = session.post(
            login_url, json={"login": self.USUARIO, "password": self.SENHA}
        )
        data = response.json()
        token = data["token"]
        session.headers.update({"Authorization": f"Bearer {token}"})
        return session

    def getLogger(self):
        logging.basicConfig()
        logger = logging.getLogger("plone-manager")
        logger.setLevel(logging.INFO)
        return logger

    def cadastraConteudos(self, conteudos):
        for path in conteudos:
            data = conteudos[path]
            parent_path = "/".join(path.split("/")[:-1])[1:]
            response = self.session.get(f"{self.BASE_URL}/{path}")

            if response.status_code == 404:
                payload = {}
                payload.update(data)
                response = self.session.post(
                    f"{self.BASE_URL}/{parent_path}", json=payload
                )
                if response.status_code > 300:
                    breakpoint()
                    self.logger.error(
                        f"Error ao criar '{path}': {response.status_code}"
                    )
                    continue
                else:
                    self.logger.info(f"Conteúdo criado: '{path}' Tipo: {data['@type']}")
            else:
                self.logger.info(f"Conteúdo existente: '{path}'")

            # Estado da publicação
            dados = response.json()

            if dados["review_state"] == "private":
                payload = {"comment": "Transição feita na importação"}
                response = self.session.post(
                    f"{self.BASE_URL}/{path}/@workflow/publish", json=payload
                )
                if response.status_code > 200:
                    self.logger.error(
                        f"Error ao transicionar '{path}' para publicado: {response.status_code}"
                    )
                    continue
                # else:
                #     logger.info(f"Conteúdo publicado: '{path}'")
            # else:
            #     logger.info(f"Conteúdo não publicado: '{path}'")
