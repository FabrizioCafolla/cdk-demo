import aws_cdk as cdk
import aws_cdk.assertions as assertions

from cdk_demo.cdk_demo_stack import CdkDemoStack


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_demo/cdk_demo_stack.py
def test_s3_created():
    app = cdk.App()
    env = cdk.Environment(account='2383838383', region='us-west-2')
    stack = CdkDemoStack(app, 'cdk-demo', env=env)
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        'AWS::S3::Bucket', {'BucketName': 'demo-2383838383-staging-us-west-2'})
