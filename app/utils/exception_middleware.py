from http import HTTPStatus

from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.utils.custom_exception import CustomHTTPException
from app.utils.utils import Utils


# custom exception handler
async def custom_http_exception_handler(
    request: Request,
    exc: CustomHTTPException,
) -> JSONResponse:
    status_code = getattr(exc, "status_code", status.HTTP_500_INTERNAL_SERVER_ERROR)
    message = getattr(exc, "message", str(exc))
    error = HTTPStatus(status_code).phrase
    return await return_response(
        status_code,
        message,
        error,
        request.url.path,
    )


# return response
async def return_response(
    status_code,
    message,
    error,
    path,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "timestamp": Utils.get_current_time(),
            "status": status_code,
            "message": message,
            "error": error,
            "path": path,
        },
    )
