from hoi.compre import Thing


def give_blabla(cls):

    class Blabla(Thing):
        pass

        def __str__(self):
            return "Blabla"

    Blabla.__init__ = cls.__init__

    cls.blabla = 49
    return cls

@give_blabla
class Hoi:

    def __init__(self, hoi):
        self.hoi = hoi


print(Hoi.blabla)
