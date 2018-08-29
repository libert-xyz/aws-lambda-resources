from chalice import Chalice
import boto3
import json
from botocore.exceptions import ClientError
from chalicelib.form import form_write

app = Chalice(app_name='form-s3')


@app.route('/')
def index():
    return {'staus': 'healthy'}

@app.route('/form', methods=['POST'], cors=True)
def form_file():

    ######  Variables ########
    bucket_name = 'dab-files'
    folder_name = ''
    filename = 'mrcplnewpats.pipe'
    #############################

    data_as_json = app.current_request.json_body
    return form_write(bucket_name,folder_name,filename,data_as_json)

@app.route('/wpl', methods=['POST'], cors=True)
def wpl_form_file():

    ######  Variables ########
    bucket_name = 'dab-files'
    folder_name = 'WPL'
    filename = 'mrcplnewpats.pipe'
    #############################

    data_as_json = app.current_request.json_body
    return form_write(bucket_name,folder_name,filename,data_as_json)

@app.route('/kpl', methods=['POST'], cors=True)
def kpl_form_file():

    ######  Variables ########
    bucket_name = 'dab-files'
    folder_name = 'KPL'
    filename = 'mrcplnewpats.pipe'
    #############################

    data_as_json = app.current_request.json_body
    return form_write(bucket_name,folder_name,filename,data_as_json)
