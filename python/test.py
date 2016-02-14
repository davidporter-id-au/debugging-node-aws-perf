import boto3
import time
import timeit

#ARGHGHGHGHG!!!! 
#Python3 is hanging when I redirect stdout! FML
# SHitty Workaround!!

def main(): 
    results=""
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

    for x in range(0, 150): 
        result = (timeit.timeit(getRecord, number=1) * 1000)
        print(result)
        results += str(result) + "\n"
        time.sleep(1)
    
    text_file = open("output.log", "w")
    text_file.write(results)
    text_file.close()

main()
