from aws_cdk import cdk


class CdkPipelineStack(cdk.Stack):

    def __init__(self, app: cdk.App, id: str, **kwargs) -> None:
        super().__init__(app, id)

        # The code that defines your stack goes here
