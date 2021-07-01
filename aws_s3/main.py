import boto3
from pprint import pprint
import json
import pandas as pd

s3_client = boto3.client('s3')

bucket_list = s3_client.list_buckets()
#pprint([item['Name'] for item in bucket_list['Buckets']])

bucket_name = 'data-eng-resources'
bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name,
    Prefix='python' # allows you to limit the number of objects that Python will return, good if there are lots of objects
)
#pprint(bucket_contents)

key_name = [item['Key'] for item in bucket_contents['Contents']]
#pprint(key_name)

s3_resource = boto3.resource('s3') # higher level of info provided
bucket = s3_resource.Bucket(bucket_name)
# print(bucket)
# objects = bucket.objects # object oriented. contains object collection manager
# print(objects)
# contents = objects.all() # this is not capped at 1000
# print(contents) # another object called contents collection
# for object in contents:
#     print(object.key)

# keys = [o.key for o in s3_resource.Bucket(bucket_name).objects.all()]
# print(keys)

# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/chatbot-intent.json'
# )
# # pprint(s3_object, sort_dicts=False)
#
# s3_data = s3_object['Body']
# strbody = s3_data.read()
# pprint(json.loads(strbody), sort_dicts=False) # turns strbody into a readable form that is not in binary BSON --> JSON

s3_happy_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/happiness-2019.csv'
)

s3_happy_data = s3_happy_object['Body']
df = pd.read_csv(s3_happy_data)
pprint(df)