import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key
# import requests

def lambda_handler(event, context):
  body = json.loads(event['body'])
  # print(event['body'])
  username = body['username']
  print(username)
  res = search_user(username)
  return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST"
    },
    "body": json.dumps({
      "message": 'Success',
      "user": res
    }),
  }

def search_user(username):
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')
  response = usersTable.scan(
    FilterExpression= 'userName = :r',
    ExpressionAttributeValues= {
      ':r': username
    }
  )
  return response