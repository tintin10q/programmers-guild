
from typing import TypedDict, Literal, List, Self


class MyClass[T]:

    def __init__(self, hello: T, world:T):
        self.l : list[T] = []

    def push(self, item: T) -> Self:
        self.l.append(item)
        return self

    def pop(self) -> T:
        return self.l.pop()


c = MyClass[int]( True,4)
c.push(4)
c.push("4")
print(c.l)





Hoi = TypedDict("Hoi", {"hoi": int, "daar": str})

def get_daar(a: Literal[3, '3'] | Hoi):

    return a

get_daar(3)







