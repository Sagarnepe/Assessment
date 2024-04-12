from google.cloud import storage
from fastapi import UploadFile, status
from app.utils.custom_exception import CustomHTTPException
from app.utils.constants import GCP_BUCKET_NAME, GCP_JSON_CRED_PATH

class GCPUpload:
    def __init__(self) -> None:
        pass

    @classmethod
    async def gcp_upload(
        cls,
        file: UploadFile
    ) -> str:
        try:
            client = storage.Client.from_service_account_json(GCP_JSON_CRED_PATH)
            
            bucket = client.bucket(GCP_BUCKET_NAME)
            destination_blob_name = file.filename
            blob = bucket.blob(destination_blob_name)
            blob.upload_from_file(file.file)
            
            url = f"https://storage.googleapis.com/{GCP_BUCKET_NAME}/{destination_blob_name}"
            
            return url
        except Exception as e:
            raise CustomHTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, 
                str(e)
            )
