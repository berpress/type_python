# Types: https://docs.pydantic.dev/latest/usage/types/
from enum import Enum
from uuid import UUID
from pydantic import BaseModel

class GenderType(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'

class Gender(BaseModel):
    gender: GenderType = GenderType.UNKNOWN


class User(BaseModel):
    id: int
    name: str | None
    friends: list[str] | None = None
    gender: Gender = Gender(gender=GenderType.UNKNOWN)


user = User(id=1234, name='Mike')
print(user)


class User2(BaseModel):
    id: UUID | int | str
    name: str


user_03_uuid = UUID('cf57432e-809e-4353-adbd-9d5c0d733868')
user_03 = User(id=user_03_uuid, name='John Doe')
print(user_03)
