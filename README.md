# type_python

### Start

Python is both a strongly typed and a dynamically typed language. Strong typing means that variables do have a type and that the type matters when performing operations on a variable. Dynamic typing means that the type of the variable is determined only during runtime.

This repository shows working with typed python

We will use

* Type hinting
* Library Paydantic
* MyPy

## Type hinting

url: https://mypy.readthedocs.io/en/stable/getting_started.html

Simple types

```python
a: int = 0
b: str = 'hello world'
...
```

Generic types

```python
list[str] = ['a', 'b]
tuple[int, int]
dict[str, int] = {'a': 1, 'b': 2}
Iterable[int] = [1, 2]
...
```

Functions

```python
def stringify(num: int) -> str:
    return str(num)
```

Classes

```python
class BankAccount:
    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters.
        self.account_name = account_name
        self.balance = initial_balance

    # For instance methods, omit type for "self"
    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

account: BankAccount = BankAccount("Alice", 400)
```

Class types

```python
class A:
    def f(self) -> int:  # Type of self inferred (A)
        return 2

class B(A):
    def f(self) -> int:
        return 3

    def g(self) -> int:
        return 4


def foo(a: A) -> None:
    print(a.f())  # 3
    a.g()         # Error: "A" has no attribute "g"


foo(B())  # OK (B is a subclass of A)
```

Prootocol

```python
from typing import Iterable
from typing_extensions import Protocol

class SupportsClose(Protocol):
    # Empty method body (explicit '...')
    def close(self) -> None:
        pass

class Resource:  # No SupportsClose base class!

    def close(self) -> None:
        pass

    # ... other methods ...

def close_all(items: Iterable[SupportsClose]) -> None:
    for item in items:
        item.close()


close_all([Resource(), open('some/file')])  # Okay!

```

Generic functions

```python
from typing import List, TypeVar

T = TypeVar("T")

def first(container: List[T]) -> T:
    return container[0]
  
if __name__ == "__main__":
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))
    
    list_two: List[int] = [1, 2, 3]
    print(first(list_two))
```

## Paydantic

Models
```python
from enum import Enum
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
    gender: Fender = Gender = Field(None, alias='Gender')


user = User(id=1234, name='Mike')
print(user)
```

Validators
```python
from pydantic import BaseModel, validator


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)
print(user)
```

Model Config

```python
from pydantic import BaseModel, Extra, ValidationError


class Model(BaseModel):
    v: str

    class Config:
        max_anystr_length = 10
        error_msg_templates = {
            'value_error.any_str.max_length': 'max_length:{limit_value}',
        }


try:
    Model(v='x' * 20)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    v
      max_length:10 (type=value_error.any_str.max_length; limit_value=10)
    """


class ModelA(BaseModel, extra=Extra.forbid):
    a: str


model_dict = {'a': 'foo', 'b': 'bar'}

try:
    ModelA(**model_dict)
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    b
      extra fields not permitted (type=value_error.extra)
    """
```

Schema

```python
from enum import Enum
from pydantic import BaseModel, Field


class FooBar(BaseModel):
    count: int
    size: float = 0


class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'
    not_given = 'not_given'


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    foo_bar: FooBar = Field(...)
    gender: Gender = Field(None, alias='Gender')
    snap: int = Field(
        42,
        title='The Snap',
        description='this is the value of snap',
        gt=30,
        lt=50,
    )

    class Config:
        title = 'Main'

# this is equivalent to json.dumps(MainModel.schema(), indent=2):
print(MainModel.schema_json(indent=2))
```

Exporting models

```python
from pydantic import BaseModel


class BarModel(BaseModel):
    whatever: int


class FooBarModel(BaseModel):
    banana: float
    foo: str
    bar: BarModel


m = FooBarModel(banana=3.14, foo='hello', bar={'whatever': 123})

# returns a dictionary:
print(m.dict())
"""
{
    'banana': 3.14,
    'foo': 'hello',
    'bar': {'whatever': 123},
}
"""
```