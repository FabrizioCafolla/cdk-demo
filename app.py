#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_demo.cdk_demo_stack import CdkDemoStack

app = cdk.App()

region = os.getenv('CDK_DEFAULT_REGION')
account_id = os.getenv('CDK_DEFAULT_ACCOUNT')
environment = os.getenv('ENVIRONMENT')

if region not in ['eu-west-1']:
    raise Exception(f'CDK_DEFAULT_REGION must be eu-west-1, but is: {region}')

if environment is None:
    raise Exception(f'var ENVIRONMENT is not set')

CdkDemoStack(
    app,
    construct_id='CdkDemoStack',
    stack_name='CdkDemoStack',
    description='Demo stack with cdk',
    env=cdk.Environment(account=account_id, region=region),
    synthesizer=cdk.DefaultStackSynthesizer(
        qualifier='demo',
        file_assets_bucket_name=f'{account_id}-cdk-demo-toolkit',
    ),
    parameters={
        'environment': environment
    }
)

app.synth()
