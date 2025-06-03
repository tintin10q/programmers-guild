

def text():
    yield from iter('hallooo daar')

stream = text()

a = 1,2,4,5
print(a)

class Hoi:

    __slots__ = "a", "b"

    def __init__(self, a: int):
        self.a = a

    def __add__(self, other):

        if not isinstance(other, Hoi) and not isinstance(other, int):
            raise NotImplementedError()

        return Hoi(self.a + int(other))

    def __ne__(self):
        raise NotImplemented()

    def __eq__(self, other):

    def __invert__(self):

    def __int__(self):
        return self.a

    def __matmul__(self, other):
        return self + other

    def __dir__(self):
        return ["niet_waar"]

    def __str__(self):
        return f"Hoi({self.a})"


a = Hoi(3)

a.a = 15

match a:

    case str():
        print("A was 3")

    case Hoi():
        print("A was niet 3")

if not joij:



