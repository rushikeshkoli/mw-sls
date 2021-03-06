# Welcome to your CDK TypeScript project!

This is a codepipeline project for TypeScript development with CDK.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

### CDK Installation
run `npm install -g aws-cdk`

## Useful commands

 * `npm run build`   compile typescript to js
 * `npm run watch`   watch for changes and compile
 * `npm run test`    perform the jest unit tests
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk synth`       emits the synthesized CloudFormation template


**Note: Please create secret in secrete manager for github auth token**

### Github Personal Access Token
You can generate github token by visiting [Github](https://github.com/settings/tokens/new).
Please tick `repo` and `admin:repo_hook` under scopes.
Then create AWS secret with any name and choose
key-value pair. Enter `git` as your key and enter `your generated token value`
as value

Enter key and value without quotes in AWS console

Enter Generated ARN by after creating secret in `./pipeline/lib/pipeline-stack.ts` at 
line 7 for value of `ARN`.
Also modify `GITHUB_OWNER`, `GITHUB_REPO_BACKEND`, `GITHUB_REPO_FRONTEND`. 
You can take look at already present values. Enter only repository value without domain and username.

### Deploying the infrastructure
*  To deploy first install dependencies using: `npm install`. (errors might occur for dev dependencies. You can continue to next step)
*  Build project using: `npm run build`
*  To deploy the infrastructure run: `cdk deploy --all`
*  To get backend url check output in `sam-app` stack in cloudformation.
*  To get S3 url check output in `frontend` stack.

### Configuring Frontend
* Visit frontend: [React](https://github.com/rushikeshkoli/mw-react)
* Edit .env file with backend url from above step.