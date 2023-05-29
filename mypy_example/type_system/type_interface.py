# mypy: ignore-errors
# This is a test file, skipping type checking in it.

from typing import Any


# Compatibility of container types
l: list[int] = []       # Create empty list of int
d: dict[str, int] = {}  # Create empty dictionary (str -> int)


def foo(arg: list[int]) -> None:
    print('Items:', ''.join(str(a) for a in arg))


foo([])  # OK


def foo2(arg: list[int]) -> None:
    print('Items:', ', '.join(arg))


a = []  # Error: Need type annotation for "a"
foo2(a)


# Other ways to silence errors

def f(x: Any, y: str) -> None:
    x = 'hello'
    x += 1  # OK
