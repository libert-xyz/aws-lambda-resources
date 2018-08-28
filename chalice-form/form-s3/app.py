from chalice import Chalice
import boto3
import json
from botocore.exceptions import ClientError

app = Chalice(app_name='form-s3')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/form', methods=['POST'], cors=True)
def form_file():
    #json example
    #data_as_json = {"name":"paul","last_name":"lennon","email":"me@beatles.com"}
    try:
        s3 = boto3.client('s3')
        s3_bucket = 'dab-files'
        file_name = 'mrcplnewpats.pipe'
        obj = s3.get_object(Bucket=s3_bucket, Key=file_name)

        #Read Current File
        j = (obj['Body'].read().decode('utf-8'))

        data_as_json = app.current_request.json_body

        #New Data
        d = data_as_json['name']+'|'+data_as_json['last_name']+'|'+data_as_json['email']
        newstr = str(j) + '\n' + d

        #Write/Update New Data
        s3.put_object(Body=newstr, Bucket=s3_bucket, Key=file_name)
        return {"status":newstr}

    except ClientError as e:
        return {'status':e.response['Error']['Message']}
