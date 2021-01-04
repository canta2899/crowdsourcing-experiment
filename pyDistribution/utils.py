import os
import boto3
import json
import credentials


def s3Init():
    return boto3.resource(
        's3',
        aws_access_key_id=credentials.worker_key_id,
        aws_secret_access_key=credentials.worker_access_key
    )


def downloadWorkers(s3, bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.download_file('ProgettoSocialComputing2/Batch1/Task/workers.json', './workers.json')
    print('Workers downloaded from S3')


def uploadWorkers(s3, bucket_name):
    bucket = s3.Bucket(bucket_name)
    bucket.upload_file('./workers.json', 'ProgettoSocialComputing2/Batch1/Task/workers.json')
    print('Workers uploaded cmd S3')


def serialize_json(filename, data):
    with open(filename, "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data serialized cmd path: {filename}")


def read_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf8") as file:
            data = json.load(file)
        print(f"Data read from path: {file_path}")
        return data
    else:
        print(f"No data found at path: {file_path}")
        return {}
