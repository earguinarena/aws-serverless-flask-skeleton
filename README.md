# README #

# AWS Serverless with Flask skeleton
Sample Serverless project with Flash using aws: lambda, api gateway, dynamodb and cognito 

### Download project
git clone https://github.com/earguinarena/aws-serverless-flask-skeleton.git

### Requirements:
* npm
* python 3.8
* aws cli


### Serverless Environment
Install the Serverless framework
```
npm install -g serverless
```

Install required serverless packages 
```
npm install or npm ci
```

### Python Environment
```
virtualenv venv --python=python3 
source venv/bin/activate 
pip install boto3 Flask==1.1.2 flask-cors==3.0.10 jsonschema==3.2.0 Werkzeug==1.0.1
```


### Setup AWS Credentials

* Install Aws cli https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
* Configure https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html
  
```
  aws configure 
```

### Deploy the project on AWS
This command deploy all the project, creating the DynamoDb Table, Lambda Function, Api gateway and Cognito.
After the execution, you can get the endpoint Ex. https://xxxxxxx.execute-api.us-east-1.amazonaws.com/dev/

By default, the stage is dev
```
sls deploy
```

Deploy in other stage
```
sls deploy -s other_stage
```  

### Mock
Execute local mock
```
sls wsgi  serve
```
or with port
```
sls wsgi serve -p 8000
```

### Invoke local lambda 
(you have to change the stage on the table name. Ex. other_stage-Example)
```
source venv/bin/activate
sls invoke local -f mainHandler --env EXAMPLE_TABLE=dev-Example --path event.json
```

## Cognito

### List Cognito user-pool-id
```
aws cognito-idp list-user-pools --max-results 20
```


### Create a Cognito User
Require:
* __user_pool_id__
* __user__
* __user_email__
```
aws cognito-idp admin-create-user \
--user-pool-id __user_pool_id__ \
--username __user__
--user-attributes Name=email,Value=__user_email__
```

### List Cognito client-id
Require:
* __user_pool_id__
```
aws cognito-idp  list-user-pool-clients \
--user-pool-id __user_pool_id__
```

### Get JWT token
Require:
* __APP_CLIENT_ID__ from cognito
* __region__ Ex. us-east-1
* __user__
* __password__
```
aws cognito-idp initiate-auth \
--client-id __APP_CLIENT_ID__ \
--region=__region__ \
--auth-flow USER_PASSWORD_AUTH \
--auth-parameters USERNAME=__user__,PASSWORD=__password__
```

#### If the previous command has NEW_PASSWORD_REQUIRED challenge
Require:
* __APP_CLIENT_ID__ from cognito
* __region__ Ex. us-east-1
* __user__
* __new_password__
* __session_id__ from the previous

```
aws cognito-idp respond-to-auth-challenge \
--client-id __APP_CLIENT_ID__ \
--region=__region__ \
--challenge-name  NEW_PASSWORD_REQUIRED \
--challenge-responses USERNAME=__user__,NEW_PASSWORD=__new_password__
--session  "__session_id__"
```
