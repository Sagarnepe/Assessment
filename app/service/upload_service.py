import requests

from typing import List, Union
from fastapi import UploadFile, Response, Header, status
from app.utils.logger import logger
from app.utils.string_responses import (
    MULTIPLE_UPLOAD_ERROR, 
    EMPTY_FILE_ERROR,
    INVALID_PROVIDER_ERROR,
    )
from app.utils.custom_exception import CustomHTTPException

from app.models.api_model import SuccessResponseModel
from app.utils.utils import Utils
from app.utils.constants import LOCAL_PATH
from app.utils.check_provider import check_provider
from app.utils.upload_util.aws_upload import AWSUpload
from app.utils.upload_util.gcp_upload import GCPUpload
from app.utils.upload_util.local_upload import LocalUpload

aws_upload = AWSUpload()
gcp_upload = GCPUpload()
local_upload = LocalUpload(LOCAL_PATH)

class UploadService:
    def __init__(self) -> None:
        pass

    @classmethod
    async def upload_schema(
        cls,
        file: List[UploadFile],
        user_id: str = Header(...)
    ) -> Union[SuccessResponseModel, Response]:
        try:
            if len(file) > 1 :
                logger.exception(MULTIPLE_UPLOAD_ERROR)
                raise CustomHTTPException(
                    status.HTTP_400_BAD_REQUEST, MULTIPLE_UPLOAD_ERROR
                )
            
            file = file[0]
            if file.size == 0:
                logger.exception(EMPTY_FILE_ERROR)
                raise CustomHTTPException(
                    status.HTTP_400_BAD_REQUEST,
                    EMPTY_FILE_ERROR
                )

            if not check_provider(user_id):
                logger.exception(INVALID_PROVIDER_ERROR)
                raise CustomHTTPException(status.HTTP_400_BAD_REQUEST, INVALID_PROVIDER_ERROR)
            
            response = None

            if 'aws' in user_id.lower():
                response = await aws_upload.aws_upload(file)

            if 'gcp' in user_id.lower():
                response = await gcp_upload.gcp_upload(file)

            if 'local' in user_id.lower():
                response = await local_upload.local_upload(file)

            if response is None:
                raise CustomHTTPException(status.HTTP_400_BAD_REQUEST, "Invalid provider")

            return SuccessResponseModel(
                    timestamp=Utils.get_current_time(),
                    status=status.HTTP_200_OK,
                    message="Object uploded successfully.",
                    data=response
                )

        except requests.exceptions.RequestException as e:
            logger.exception(f"{str(e)}")
            raise CustomHTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
