def sub_generator(start, end):
    """A simple generator that yields values from start to end-1."""
    for i in range(start, end):
        msg = yield i
        if msg is not None:
            print("Got msg", msg)


def main_generator(ranges: list[tuple[int, int]]):
    """A generator that delegates to sub_generator using yield from."""
    print("Main generator starting")

    for start, end in ranges:
        print(f"Delegating to sub_generator({start}, {end})")
        # yield from delegates iteration to another generator
        result = yield from sub_generator(start, end)
        print(f"Back in main_generator after sub_generator({start}, {end}) {result}")

    print("Main generator completed")


# Use the generator
ranges = [(1, 4), (10, 13)]
gen = main_generator(ranges)

# Consume values from the generator
for value in gen:

    if value == 10:
        gen.send("Hoii")
        gen.send("Hoii222")
        gen.send("Hoii23")
        gen.send("Hoii2333")
    print(f"Got value: {value}")