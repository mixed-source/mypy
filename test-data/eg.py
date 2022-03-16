import abc
# from typing import Callable
from collections.abc import Callable


class A(abc.ABC):
    @abc.abstractmethod
    def m(self) -> None:
        ...


class C(A):
    def m(self) -> None:
        pass


def f() -> A:
    return C()


def t(x: Callable[[], A]) -> None:
    x()


def main() -> None:
    t(f)
    t(C)
    print(callable(A))
    t(A)  # should give typing error - A is not callable because it can't be instantiated
    # A()  # mypy correctly reports that A can't be instantiated


if __name__ == "__main__":
    main()
