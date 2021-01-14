import json
import boto3
# import requests

def lambda_handler(event, context):
  users = get_users()
  return {
    "statusCode": 200,
    "body": json.dumps({
      "message": ['a', 'b'],
      "users": users
    }),
  }

def get_users():
  dynamodb = boto3.resource('dynamodb')

  usersTable = dynamodb.Table('users_table1')

  all_users = usersTable.scan()
  print(all_users)
  return all_users