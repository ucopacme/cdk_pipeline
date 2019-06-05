#!/usr/bin/env python3

from aws_cdk import cdk

from cdk_pipeline.cdk_pipeline_stack import CdkPipelineStack


app = cdk.App()
CdkPipelineStack(app, "cdk-pipeline-cdk-1")

app.run()
