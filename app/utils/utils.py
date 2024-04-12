from datetime import datetime, timezone

import pytz

KATHMANDU_TIMEZONE = pytz.timezone("Asia/Kathmandu")


class Utils:
    """
    Utility classes
    """

    def __init__(self):
        pass

    @staticmethod
    def get_current_time() -> str:
        """
        Returns current date time
        """
        utc_now = datetime.now(timezone.utc)
        kathmandu_datetime = utc_now.astimezone(KATHMANDU_TIMEZONE)
        return kathmandu_datetime.isoformat()

