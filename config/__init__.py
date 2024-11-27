import os
import boto3


class SSMParameterRetriever:
    def __init__(self):
        self.aws_region_name = "ap-northeast-1"
        self.ssm_client = boto3.client("ssm", region_name=self.aws_region_name)
        self.env = os.environ.get("FLASK_ENV", "develop")
        self.ssm_root = f"/backend/service/api-{self.env}"

    def get_parameter(self, suffix):
        """
        Retrieve a parameter from SSM with decryption.

        Args:
            suffix (str): The suffix to append to the SSM root path.

        Returns:
            str: The value of the requested SSM parameter.
        """
        response = self.ssm_client.get_parameter(
            Name=self.ssm_root + suffix, WithDecryption=True
        )
        return response["Parameter"]["Value"]


ssm_retriever = SSMParameterRetriever()


ENV = os.environ.get("FLASK_ENV", "develop")
if ENV == "production":
    from config.production import *
elif ENV == "staging":
    from config.staging import *
else:
    from config.develop import *
