import json
import boto3
import uuid
# import requests

def lambda_handler(event, context):
  body = json.loads(event['body'])
  # print(event['body'])
  username = body['username']
  delete_user(username)
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": 'Success',
    }),
  }

def delete_user(username):
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')
  response = usersTable.delete_item(
    Key = {
      "userId": username
    }
  )
  return