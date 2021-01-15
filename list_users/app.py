import json
import boto3


# import requests

def lambda_handler(event, context):
    users = get_users()
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


def get_users():
    dynamodb = boto3.resource('dynamodb')

    users_table = dynamodb.Table('users_table1')
    all_users = users_table.scan()
    user_names = []
    for user in all_users['Items']:
        print(user['userName'])
        user_names.append(user['userName'])

    print(user_names)
    return user_names
