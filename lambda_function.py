import json
import sys
import os
import requests

def lambda_handler(event, context):
    # TODO implement
    print("****************Start*****************************")

    print("hello dalia")
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
if __name__ == "__main__":
    lambda_handler({}, {})
