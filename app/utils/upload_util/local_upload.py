import os
from fastapi import UploadFile

class LocalUpload:
    def __init__(self, local_path: str) -> None:
        self.local_path = local_path

    async def local_upload(
        self,
        file: UploadFile
    ) -> str:
        file_path = os.path.join(self.local_path, file.filename)

        with open(file_path, "wb") as local_file:
            local_file.write(await file.read())

        return file_path