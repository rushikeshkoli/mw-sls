import json
import boto3
import uuid
# import requests

def lambda_handler(event, context):
  body = json.loads(event['body'])
  # print(event['body'])
  username = body['username']
  image_url = 'url'
  desc = body['desc']
  add_user(username, image_url, desc)
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": 'Success'
    }),
  }


def add_user(username, image_url, desc):
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')

  usersTable.put_item(
    Item={
      'userId': str(uuid.uuid1()),
      'userName': username,
      'imageUrl': image_url,
      'description': desc
    }
  )
  return