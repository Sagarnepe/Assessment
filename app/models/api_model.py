
from pydantic import BaseModel


class ResponseModel(BaseModel):
    """
    Base class for all responses
    """

    timestamp: str
    status: int
    message: str

# success response model
class SuccessResponseModel(ResponseModel):
    """
    Base class for success response
    """

    data: str