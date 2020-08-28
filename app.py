#!/usr/bin/env python3

from aws_cdk import core

from cdk_cloudfront_origin.cdk_cloudfront_origin_stack import CdkCloudfrontOriginStack


app = core.App()
CdkCloudfrontOriginStack(app, "cdk-cloudfront-origin", env={'region': 'us-west-2'})

app.synth()
