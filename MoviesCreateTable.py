import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName' : 'year',
                'KeyType' : 'HASH',
            },
            {
                'AttributeName' : 'title',
                'KeyType' : 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
)
print('Table status:', table.table_status)

print('waiting for', table.name, 'to complete creating....')
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')
print('Table status:', dynamodb.Table('Movies').table_status)

