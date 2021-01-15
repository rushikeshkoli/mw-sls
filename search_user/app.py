import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key
# import requests

def lambda_handler(event, context):
  body = json.loads(event['body'])
  # print(event['body'])
  username = body['username']
  res = search_user(username)
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": 'Success',
      "user": res
    }),
  }

def search_user(username):
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')
  response = usersTable.query(
    KeyConditionExpression=Key('userId').eq(username)
  )
  return response