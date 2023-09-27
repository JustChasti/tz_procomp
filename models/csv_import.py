# python system libs
from datetime import datetime
from random import randint
from typing import Tuple
# external libs
from fastapi import UploadFile
import bcrypt
# project import
from config import encrypt_salt, files_folder
from models.user_models import UserAuthModel


class CsvFile():
    def __init__(self, file: UploadFile, user: UserAuthModel) -> None:
        self.file = file
        self.filename = f"{self.file.filename}.{datetime.now()}.{randint(0, 100)}"
        self.id = bcrypt.hashpw(
            self.filename.encode('utf-8'),
            encrypt_salt
        ).decode('utf-8')
        self.user_id = user.user_id

    async def save_file(self) -> Tuple[bool, str]:
        if self.user_id:
            data = await self.file.read()
            with open(F"{files_folder}/{self.id}", "a") as f:
                f.write(data)
            return (True, f"your file id: {self.id}")
        else:
            return (False, 'Not authorized, token expired')
