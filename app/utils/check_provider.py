from app.utils.constants import ALLOWED_PROVIDERS

def check_provider(user_id: str) -> bool:
    for provider in ALLOWED_PROVIDERS:
        if user_id.lower().startswith(provider):
            return True
    return False
