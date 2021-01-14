import json
import boto3
import uuid
# import requests

def lambda_handler(event, context):
  print(event)
  add_user()
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": 'Success'
    }),
  }

def add_user():
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')

  usersTable.put_item(
    Item={
      'userId': str(uuid.uuid1()),
      'userName': 'rushi'
    }
  )
  return