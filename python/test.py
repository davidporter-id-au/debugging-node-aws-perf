import boto3
import time
import timeit

client = boto3.client('dynamodb')

def getRecord(): 
    table="test"
    key="FOO"
    response = client.get_item(
        TableName=table,
        ConsistentRead=False,
        Key={
            'key': {
                'S': key,
            }
        }
    )
    return response

while True: 
    print("Milliseconds:", (timeit.timeit(getRecord, number=1) * 1000))
    time.sleep(1)
