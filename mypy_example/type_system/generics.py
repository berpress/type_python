from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

# Construct an empty Stack[int] instance


stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push('x')  # error: Argument 1 to "push" of "Stack" has incompatible type "str"; expected "int"

# Generic functions