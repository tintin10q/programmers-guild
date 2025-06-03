
from dataclasses import dataclass

def get_data():
    a = {"hoi": 3, "daar": 4, "hierzo": [1, 2, 3,4]}
#                                                ^
# __getindex__

@dataclass
class Thing:
    hoi: int
    daar: int = 4
    hierzo: list[int] =


class Bla:

    g = 4

Bla.g

def get_thing(thing) -> Thing:
    match thing:
        case {"hoi": int(hoi), "daar": int(daar), "hierzo": list(hierzo)}:
            if not all(map(lambda x: isinstance(x, int), hierzo)):
                raise TypeError("All hierzo have to be int")

            return Thing(hoi=hoi, daar=daar, hierzo=hierzo)
        case _:
            raise ValueError(f"Unknown thing: {thing}")


def fetch_thing():

    dict_thing = get_data()
    actual_thing = get_thing(dict_thing)

    actual_thing.hierzo[0].

    match response:
        case 404 | 401:
            ...
        case 200 | 201:
            ...

print(get_thing(a))