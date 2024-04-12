import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.custom_exception import CustomHTTPException
from app.utils.exception_middleware import custom_http_exception_handler
from app. router import upload_router
app = FastAPI()

app.add_middleware(CORSMiddleware)

app.exception_handler(CustomHTTPException)(custom_http_exception_handler)

app.include_router(upload_router.router)

@app.get("/")
async def root():
    return {"message": "Hello this is a upload service for cloud."}


if __name__ == "__main__":
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000, reload=True
    )
