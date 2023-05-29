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