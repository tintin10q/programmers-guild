import json


class Persist:

    # allowed_keys = "ho", "bo"

    def __init__(self, filename: str):
        self.filename = filename
        self.data = {}
        self.allowed_keys = []

    def __enter__(self) -> dict:
       try:
           with open(self.filename, "r") as f:
               json_data = json.load(f)
               self.data = json_data
       except FileNotFoundError:
           return self.data
       return self.data

    def __exit__(self, exc_type, exc_val, exc_tb):

        for key in self.data.keys():
            if key not in self.allowed_keys:
                raise TypeError("You are trying to do something wrong!!")

        with open(self.filename, "w+") as f:
            json.dump(self.data, f)


with Persist("hoi") as hoi:
    print(hoi)
    hoi["ho"] = 4
    hoi["bo"] = 4
    hoi["yo"] = 4



