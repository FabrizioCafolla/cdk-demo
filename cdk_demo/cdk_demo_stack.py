import os

from aws_cdk import (
    Stack,
    aws_s3 as s3,
)
from constructs import Construct

class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        env = kwargs.get("env")
        if env is None:
            raise Exception("Environment is not set, pass it from app.py")

        self.stage = os.environ["ENVIRONMENT"]
        self.account = env.account
        self.region = env.region

        bucket = s3.Bucket(
            self, 
            "DemoBucket",
            bucket_name=f"{self.account}-{self.stage}-demo-bucket",
        )
        

