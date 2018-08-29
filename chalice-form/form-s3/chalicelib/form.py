import boto3
import json
from botocore.exceptions import ClientError


def form_write(bucket_name,folder,filename,data_as_json):
    #json example
    #data_as_json = {"name":"paul","last_name":"lennon","email":"me@beatles.com"}

    try:
        s3 = boto3.client('s3')
        if folder != '':
            filename = folder+"/"+filename

        obj = s3.get_object(Bucket=bucket_name, Key=filename)

        #Read Current File
        j = (obj['Body'].read().decode('utf-8'))

        #Append new data
        d = data_as_json['name']+'|'+data_as_json['last_name']+'|'+data_as_json['email']
        newstr = str(j) + '\n' + d

        #Write/Update New Data
        s3.put_object(Body=newstr, Bucket=bucket_name, Key=filename)

        return {"status":200}

    except ClientError as e:
        return {'status':e.response['Error']['Message']}
