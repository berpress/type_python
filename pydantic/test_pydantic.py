from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


new_user = User(id=1, name='Robert', friends=[1, 2, 4]) # all good
# new_user_2 = User(id=1, name='Robert', friends='Test') # got error
new_user_3 = User(id=1, name='Robert', friends=[1], age=15)
print(new_user_3.middle_name) # got error