import aws_cdk as cdk
import aws_cdk.assertions as assertions

from cdk_demo.cdk_demo_stack import CdkDemoStack

FAKE_ACCOUNT = '2383838383'
FAKE_REGION = 'us-west-2'
FAKE_ENVIRONMENT = 'staging'

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo/cdk_demo_stack.py


def test_s3_created():
    app = cdk.App()

    env = cdk.Environment(account=FAKE_ACCOUNT, region=FAKE_REGION)

    stack = CdkDemoStack(
        app,
        'cdk-demo',
        env=env,
        parameters={
            'environment': FAKE_ENVIRONMENT
        }
    )

    template = assertions.Template.from_stack(stack)

    template.has_resource_properties(
        'AWS::S3::Bucket', {'BucketName': f'demo-{FAKE_ACCOUNT}-{FAKE_ENVIRONMENT}-{FAKE_REGION}'})
