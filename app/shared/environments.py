from enum import Enum
import os

from app.modules.url_management.domain.repositories.url_repository import IURLRepository


class STAGE(Enum):
    dev = "dev"
    homol = "homol"
    prod = "prod"
    test = "test"

class Environments:

    stage: STAGE
    region: str
    dynamo_table_name: str
    dynamo_partition_key: str

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["stage"] = os.environ.get("stage") or STAGE.test.value


    def load_envs(self) :
        if "stage" not in os.environ or os.environ["stage"] == STAGE.test.value:
            self._configure_local()

        self.region = os.environ.get("AWS_REGION")
        self.dynamo_table_name = os.environ.get("DYNAMO_TABLE_NAME")
        self.dynamo_partition_key = os.environ.get("DYNAMO_PARTITION_KEY")

    @staticmethod
    def get_url_repository() -> IURLRepository:
        if Environments.get_envs().stage == STAGE.test:
            

    @staticmethod
    def get_envs() -> "Environments":
        envs = Environments()
        envs.load_envs()
        return envs