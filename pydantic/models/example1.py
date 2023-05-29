from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = 'Jane Doe'


user = User(id='123')
print(user)
