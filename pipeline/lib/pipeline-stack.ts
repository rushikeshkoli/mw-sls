import * as cdk from '@aws-cdk/core';
import s3 = require('@aws-cdk/aws-s3');
import codepipeline = require('@aws-cdk/aws-codepipeline');
import codepipeline_actions = require('@aws-cdk/aws-codepipeline-actions');
import codebuild = require('@aws-cdk/aws-codebuild');
import {CfnOutput} from "@aws-cdk/core";

const SEC = cdk.SecretValue.secretsManager('arn:aws:secretsmanager:ap-south-1:660829820053:secret:mysec-kjgGr5', {jsonField: 'git'})


export class PipelineStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const artifactsBucket = new s3.Bucket(this, "ArtifactsBucket");

// Pipeline creation starts
    const pipeline = new codepipeline.Pipeline(this, 'Pipeline', {
      artifactBucket: artifactsBucket
    });

// Declare source code as an artifact
    const sourceOutput = new codepipeline.Artifact();
// Add source stage to pipeline
    pipeline.addStage({
      stageName: 'Source',
      actions: [
        new codepipeline_actions.GitHubSourceAction({
          actionName: 'Github_Source',
          repo: 'mw-sls',
          output: sourceOutput,
          owner: 'rushikeshkoli',
          oauthToken: SEC,
          branch: 'master'
        }),
      ],
    });

    // Declare build output as artifacts
    const buildOutput = new codepipeline.Artifact();

// Declare a new CodeBuild project
    const buildProject = new codebuild.PipelineProject(this, 'Build', {
      environment: {buildImage: codebuild.LinuxBuildImage.AMAZON_LINUX_2_2},
      environmentVariables: {
        'PACKAGE_BUCKET': {
          value: artifactsBucket.bucketName
        }
      }
    });

// Add the build stage to our pipeline
    pipeline.addStage({
      stageName: 'Build',
      actions: [
        new codepipeline_actions.CodeBuildAction({
          actionName: 'Build',
          project: buildProject,
          input: sourceOutput,
          outputs: [buildOutput],
        }),
      ],
    });
    // Deploy stage
    pipeline.addStage({
      stageName: 'Dev',
      actions: [
        new codepipeline_actions.CloudFormationCreateReplaceChangeSetAction({
          actionName: 'CreateChangeSet',
          templatePath: buildOutput.atPath("packaged.yaml"),
          stackName: 'sam-app',
          adminPermissions: true,
          changeSetName: 'sam-app-dev-changeset',
          runOrder: 1
        }),
        new codepipeline_actions.CloudFormationExecuteChangeSetAction({
          actionName: 'Deploy',
          stackName: 'sam-app',
          changeSetName: 'sam-app-dev-changeset',
          runOrder: 2
        }),
      ],
    });

  }
}

export class FrontendStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const artifactsBucket = new s3.Bucket(this, "ArtifactsBucket1");
    const websiteBucket = new s3.Bucket(this, 'WebsiteBucket', {
      websiteIndexDocument: 'index.html',
      publicReadAccess: true
    });

    const imageBucket = new s3.Bucket(this, 'ImageStoreBucket', {
      publicReadAccess: true
    })

// Pipeline creation starts
    const pipeline = new codepipeline.Pipeline(this, 'Pipeline', {
      artifactBucket: artifactsBucket
    });

// Declare source code as an artifact
    const sourceOutput = new codepipeline.Artifact();
// Add source stage to pipeline
    pipeline.addStage({
      stageName: 'Source',
      actions: [
        new codepipeline_actions.GitHubSourceAction({
          actionName: 'Github_Source',
          repo: 'mw-react',
          output: sourceOutput,
          owner: 'rushikeshkoli',
          oauthToken: SEC,
          branch: 'master'
        }),
      ],
    });

    // Declare build output as artifacts
    const buildOutput = new codepipeline.Artifact();

// Declare a new CodeBuild project
    const buildProject = new codebuild.PipelineProject(this, 'Build', {
      environment: {buildImage: codebuild.LinuxBuildImage.AMAZON_LINUX_2_2},
      environmentVariables: {
        'PACKAGE_BUCKET': {
          value: artifactsBucket.bucketName
        }
      }
    });

// Add the build stage to our pipeline
    pipeline.addStage({
      stageName: 'Build',
      actions: [
        new codepipeline_actions.CodeBuildAction({
          actionName: 'Build',
          project: buildProject,
          input: sourceOutput,
          outputs: [buildOutput],
        }),
      ],
    });

    // const s3Deploy = new s3_deployment.BucketDeployment(this, 'DeployWebsite', {
    //   sources: [s3_deployment.Source.asset('./website-dist')],
    //   destinationBucket: websiteBucket,
    //   destinationKeyPrefix: 'web/static' // optional prefix in destination bucket
    // });
    // Deploy stage
    pipeline.addStage({
      stageName: 'Dev',
      actions: [
        new codepipeline_actions.S3DeployAction({
          actionName: 'CreateChangeSet',
          bucket: websiteBucket,
          input: buildOutput
        }),
      ],
    });
    new cdk.CfnOutput(this, 'url', {value: websiteBucket.bucketDomainName})
  }
}
