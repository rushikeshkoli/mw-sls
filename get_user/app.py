import json
import boto3
from boto3.dynamodb.conditions import Key


# import requests

def lambda_handler(event, context):
    print(event['pathParameters']['userId'])
    username = event['pathParameters']['userId']
    print(username)
    # username = username['userId']
    # username = 'rahul'
    # print(username)
    users = get_user(username)
    # print(username)
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
        "body": json.dumps({
            "message": ['a', 'b', 'c', 'd'],
            "users": users
        }),
    }


def get_user(username):
    dynamodb = boto3.resource('dynamodb')

    users_table = dynamodb.Table('users_table1')
    response = users_table.query(
      KeyConditionExpression=Key('userId').eq(username)
    )

    print(response['Items'])
    return response['Items'][0]
