import os

# api prefix base url
BASE_URL = os.getenv("VAR_BASE_URL")

# allowed providers
ALLOWED_PROVIDERS = os.getenv("VAR_PROVIDERS")

# s3 bucket
S3_BUCKET = os.getenv("VAR_S3_BUCKET")

# aws creds
AWS_ACCESS_KEY_ID = os.getenv("VAR_AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("VAR_AWS_SECRET_KEY")

# local path
LOCAL_PATH = "C:/Users/sagar.neupane_genese/Desktop/"

#gcp bucket
GCP_BUCKET_NAME = os.getenv("VAR_GCP_BUCKET")

#gcp credentials path
GCP_JSON_CRED_PATH = "..."