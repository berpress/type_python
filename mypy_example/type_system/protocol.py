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
