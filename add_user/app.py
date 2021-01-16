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
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')
  response = usersTable.scan(
    FilterExpression= 'userName = :r',
    ExpressionAttributeValues= {
      ':r': username
    }
  )
  if len(response['Items']) > 0:
    return {
      "statusCode": 200,
      "headers": {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Allow-Methods": "*"
      },
      "body": json.dumps({
        "message": 'failure'
      }),
    }
  res = add_user(username, image_url, desc)
  return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "*"
    },
    "body": json.dumps({
      "message": 'Success',
      "user": res
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
  response = usersTable.scan(
    FilterExpression= 'userName = :r',
    ExpressionAttributeValues= {
      ':r': username
    }
  )
  # print(response)
  return response['Items'][0]