# type_python

### Start

Python is both a strongly typed and a dynamically typed language. Strong typing means that variables do have a type and that the type matters when performing operations on a variable. Dynamic typing means that the type of the variable is determined only during runtime.

This repository shows working with typed python

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