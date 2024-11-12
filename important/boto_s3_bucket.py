import boto3

client = boto3.client("s3")

response = client.create_bucket(
    Bucket = "vrushali-s3-bucket-boto3-handson"
)

response = client.get_bucket_acl(
    Bucket = "vrushali-s3-bucket-boto3-handson"
)

print(response)