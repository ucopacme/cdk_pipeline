from aws_cdk import cdk
from aws_cdk import (
    aws_iam as iam,
    aws_codepipeline as codepipeline,
    aws_codebuild as codebuild,
)


class CdkPipelineStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        # The code that defines your stack goes here
        pipeline = codepipeline.Pipeline(self,
            kwargs['pipeline_name'],
            pipeline_name=kwargs['pipeline_name'],
        )
