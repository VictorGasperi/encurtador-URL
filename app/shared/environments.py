from enum import Enum
import os
from app.modules.url_management.domain.repositories.url_repository import IUrlRepository


class STAGE(Enum):
    dev = "dev"
    homol = "homol"
    prod = "prod"
    test = "test"

class Environments:

    stage: STAGE
    region: str
    dynamo_table_name: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv(dotenv_path='./app/.env')
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.test.value


    def load_envs(self) :

        if "STAGE" not in os.environ:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

        if self.stage == STAGE.test:
            self.region = 'us-east-1'
            self.dynamo_table_name = 'local-dybnamo-table'
        else:
            self.region = os.environ.get("AWS_REGION")
            self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")

    @staticmethod
    def get_url_repository() -> IUrlRepository:
        if Environments.get_envs().stage == STAGE.test:
            from app.modules.url_management.infrastructure.repositories.url_repository_mock import UrlRepositoryMock
            return UrlRepositoryMock
        elif Environments.get_envs().stage in [STAGE.dev, STAGE.homol, STAGE.prod]:
            print('a')
        else:
            raise Exception('Nenhum repositorio encontrado para esse ambiente')

    @staticmethod
    def get_envs() -> "Environments":
        envs = Environments()
        envs.load_envs()
        return envs