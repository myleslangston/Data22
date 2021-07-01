import boto3
import pandas as pd
import io

# retrieves a csv file called fish market mon from the data eng resources bucket
s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'
s3_fish_market_mon = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-mon.csv'
)

s3_fish_mon_data = s3_fish_market_mon['Body']  # referencing 'Body' gets the actual data we want

df_mon = pd.read_csv(s3_fish_mon_data)  # allows us to read the file within python

# retrieves a csv file called fish market tues from the data eng resources bucket
s3_fish_market_tues = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-tues.csv'
)

s3_fish_tues_data = s3_fish_market_tues['Body']  # referencing 'Body' gets the actual data we want
df_tues = pd.read_csv(s3_fish_tues_data)  # allows us to read the file within python


fish_species_mon = df_mon.groupby('Species')  # groups the fish by their species
mean_mon = fish_species_mon.mean()  # finds the average for each of the columns

fish_species_tues = df_tues.groupby('Species')  # groups the fish by their species
mean_tues = fish_species_tues.mean()  # finds the average for each of the columns

# renames the fish species names to include the day
mean_mon_con = mean_mon.rename(index=lambda s: s+' Mon')
mean_tues_con = mean_tues.rename(index=lambda s: s+' Tues')

updated_table = pd.concat([mean_mon_con, mean_tues_con], axis=0)  # concatenates the two tables
alphab_desc_updated_table = updated_table.sort_values('Species', axis=0, ascending=False, inplace=False)  # sorts the table alphabetically

# this allows me to create files within the data eng resources bucket in s3
str_buffer = io.StringIO()
alphab_desc_updated_table.to_csv(str_buffer)
s3_resource = boto3.resource('s3')
s3_resource.Object(
    'data-eng-resources',
    'Data22/fish/MylesLangston.csv'
).put(
    Body=str_buffer.getvalue()
)

