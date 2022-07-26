#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_demo.cdk_demo_stack import CdkDemoStack

app = cdk.App()

region = os.getenv('CDK_DEFAULT_REGION')
account_id = os.getenv('CDK_DEFAULT_ACCOUNT')

if region not in ['eu-west-1']:
    raise Exception(f'CDK_DEFAULT_REGION must be eu-west-1, but is: {region}')

if os.getenv("ENVIRONMENT") is None:
    raise Exception(f'var ENVIRONMENT is not set')

environment=cdk.Environment(account=account_id,region=region)

CdkDemoStack(
    app, 
    construct_id="CdkDemoStack",
    stack_name="CdkDemoStack",
    description="Demo stack with cdk",
    env=environment,
    synthesizer=cdk.DefaultStackSynthesizer(
        qualifier='demo',
        file_assets_bucket_name=f'{account_id}-cdk-demo-toolkit',
    )
)

app.synth()
