import json
import sys

def lambda_handler(event, context):
    # TODO implement
    print("****************Start*****************************")
    print("****************End*****************************")
    return {
          "isBase64Encoded": False,
          "statusCode": 200,
          "body": "Hello from Lambda!",
          "headers": {
            "content-type": "application/json",
            "X-Amz-Function-Error": True
          }
        }
