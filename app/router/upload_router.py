from typing import List,Union
from fastapi import APIRouter, UploadFile, Response, Header, status

from app.models.api_model import SuccessResponseModel
from app.service.upload_service import UploadService
from app.utils.api_endpoints import UPLOAD_ENDPOINT

router = APIRouter(prefix=UPLOAD_ENDPOINT)

upload_service = UploadService()

@router.post("/", tags=["Upload"],
             response_model=None,
    responses={
        status.HTTP_200_OK: {"model": SuccessResponseModel},
    },
)

async def upload_schema(
    file: List[UploadFile],
    user_id: str = Header(...)
) -> Union[SuccessResponseModel, Response]:
    return await upload_service.upload_schema(file, user_id)