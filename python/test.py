import boto3
import time
import timeit

def main(): 
    client = boto3.client('dynamodb', region_name='ap-southeast-2')

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

main()
