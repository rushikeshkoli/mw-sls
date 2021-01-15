import json
import boto3
import uuid
# import requests

def lambda_handler(event, context):
  body = json.loads(event['body'])
  # print(event['body'])
  username = body['username']
  image_url = body['url']
  desc = body['desc']
  update_user(username, image_url, desc)
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": 'Success'
    }),
  }

def update_user(username, image_url, desc):
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')

  usersTable.update_item(
    Key={
      'userId': username
    },
    UpdateExpression = "set imageUrl = :i, description = :d",
    ExpressionAttributeValues= {
      ":i": image_url,
      ":d": desc
    },
  )
  return