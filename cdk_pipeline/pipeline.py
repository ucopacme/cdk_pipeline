'''
import { Construct, Stack, SecretParameter } from '@aws-cdk/cdk';
import {
    Role, ServicePrincipal, Policy, PolicyStatement, PolicyStatementEffect,
} from '@aws-cdk/aws-iam';
import { Pipeline, GitHubSourceAction } from '@aws-cdk/aws-codepipeline';
import {
    Project, CodePipelineSource, LinuxBuildImage,
} from '@aws-cdk/aws-codebuild';
'''
from aws_cdk import (
    cdk,
    aws_iam as iam,
    aws_codepipeline as codepipeline,
    aws_codebuild as codebuild,
)

'''
/** Creates a single end-to-end Pipeline for a specific service definition. */
export class ServicePipeline extends Construct {
    readonly pipeline: Pipeline;

    readonly alert: PipelineFailedAlert;

    constructor(scope: Construct, id: string, props: ServicePipelineProps) {
        super(scope, id);
        const pipelineName = `${props.service.serviceName}_${props.sourceTrigger}`;
        this.pipeline = new Pipeline(scope, pipelineName, {
            pipelineName,
        });

        // https://docs.aws.amazon.com/codepipeline/latest/userguide/GitHub-rotate-personal-token-CLI.html
        const oauth = new SecretParameter(scope, 'GithubPersonalAccessToken', {
            ssmParameter: props.service.githubTokenSsmPath,
        });

        const sourceAction = new GitHubSourceAction({
            actionName: props.sourceTrigger === SourceTrigger.PullRequest ? 'GitHub_SubmitPR' : 'GitHub_PushToMaster',
            owner: props.service.githubOwner,
            repo: props.service.githubRepo,
            branch: 'master',
            oauthToken: oauth.value,
            outputArtifactName: 'SourceOutput',
        });

        this.pipeline.addStage({
            name: 'Source',
            actions: [sourceAction],
        });
'''

class ServicePipeline(cdk.Construct):

    def __init__(self, scope: cdk.Construct, id: str, props: dict) -> None:
        super().__init__(scope, id)

        self.pipeline = codepipeline.Pipeline(self,
            props['pipeline_name'],
            pipeline_name=props['pipeline_name'],
        )

