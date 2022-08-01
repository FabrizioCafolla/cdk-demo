from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from constructs import Construct


class CdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        self.parameters = kwargs.pop('parameters', {})

        super().__init__(scope, construct_id, **kwargs)

        self.stage = self.parameters.get('environment')

        s3.Bucket(
            self,
            'DemoBucket',
            bucket_name=f'demo-{self.account}-{self.stage}-{self.region}',
        )
