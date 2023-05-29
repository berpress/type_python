def greet_all(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)   # Ok!
greet_all(ages)    # Error due to incompatible types

from collections.abc import Iterable
from pathlib import Path  # or "from typing import Iterable"


def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)
        
from typing import Union


def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id
    
# from pathlib import Path


def load_template(template_path: Path, name: str) -> str:
    # Mypy knows that `file_path` has a `read_text` method that returns a str
    template = template_path.read_text()
    # ...so it understands this line type checks
    return template.replace('USERNAME', name)