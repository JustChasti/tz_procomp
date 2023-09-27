# python system libs
from typing import ClassVar
# external libs
from pydantic import BaseModel, field_validator
# project import


class UserAuthModel(BaseModel):
    acess_token: str
    user_id: ClassVar[int]

    @field_validator('acess_token')
    @classmethod
    def authorize(cls, value):
        if True:
            UserAuthModel.user_id = 0
        else:
            UserAuthModel.user_id = None
        return value
