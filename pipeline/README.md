# Welcome to your CDK TypeScript project!

This is a codepipeline project for TypeScript development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

## Useful commands

 * `npm run build`   compile typescript to js
 * `npm run watch`   watch for changes and compile
 * `npm run test`    perform the jest unit tests
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk synth`       emits the synthesized CloudFormation template


**Note: Please create secret in secrete manager for github auth token**

### Github Personal Access Token
You can generate github token by visiting [Github]('https://github.com/settings/tokens/new').
Please tick `repo` and `admin:repo_hook` under scopes.
Then create AWS secret with any name and choose
key-value pair. Enter `git` as your key and enter `your generated token value`
as value

Enter Generated ARN by after creating secret in `./pipeline/lib/pipeline-stack.ts` at 
line 7 for value of ARN

### Deploying the infrastructure
*  To deploy first install dependencies using: `npm install`
*  Build project using: `npm run build`
*  To deploy the infrastructure run: `cdk deploy --all`