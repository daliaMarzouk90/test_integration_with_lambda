import json
import sys

my_input = os.environ["INPUT_MYINPUT"]

def lambda_handler(event, context):
    # TODO implement
    print("****************Start*****************************")
    my_input = os.environ["INPUT_MYINPUT"]
    my_output = f"Hello {my_input}"
    print(f"::set-output name=myOutput::{my_output}")
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
