import boto3

from io import BytesIO
from typing import Dict, Union
from fastapi import UploadFile, status

from app.utils.custom_exception import CustomHTTPException
from app.utils.constants import (
    S3_BUCKET,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    )


class AWSUpload:
    def __init__(self) -> None:
        pass

    @classmethod
    async def aws_upload(
        cls,
        file: UploadFile
    ) -> None:
        print("inside")
        filename = file.filename
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )
        try:
            # Read the content of the UploadFile object
            file_content = await file.read()

            # Upload file to S3
            s3.put_object(Body=file_content, Bucket=S3_BUCKET, Key=filename)

            presigned_url = s3.generate_presigned_url(
                "get_object",
                Params={"Bucket": S3_BUCKET, "Key": filename},
                ExpiresIn=3600,
            )
            return presigned_url
        except Exception as e:
            raise CustomHTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, 
                str(e)
            )