from app.utils.constants import BASE_URL


def get_endpoint(resource: str) -> str:
    return f"{BASE_URL}/{resource}"


UPLOAD_ENDPOINT = get_endpoint("upload")