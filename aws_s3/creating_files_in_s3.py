import boto3
import json

s3_client = boto3.client('s3')

my_dict = {
    'name': 'Myles',
    'age': 24,
    'understanding': False
}
#
# with open('MylesLangston.json', 'w') as jsonfile:
#     json.dump(my_dict, jsonfile)
#
# s3_client.upload_file( # allows you to upload a file to aws s3 machine
#     Filename='MylesLangston.json',
#     Bucket='data-eng-resources',
#     Key='Data22/test/MylesLangston.json'
# )
#
# s3_client.put_object(
#     Bucket='data-eng-resources',
#     Key='Data22/test/MylesLangston2.json',
#     Body=json.dumps(my_dict)
# )
# print(json.dumps(my_dict))

import pandas as pd
import io

df = pd.DataFrame([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
str_buffer = io.StringIO()
df.to_csv(str_buffer)

# s3_client.put_object(
#     Bucket='data-eng-resources',
#     Key='Data22/test/MylesLangston.csv',
#     Body=str_buffer.getvalue()
# )

s3_resource = boto3.resource('s3')
s3_resource.Object(
    'data-eng-resources',
    'Data22/test/MylesLangston2.csv'
).put(
    Body=str_buffer.getvalue()
)
