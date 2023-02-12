import datetime
import uuid
import json
import os.path


class Testcode:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.name = 'Name'
        self.test = 'correct'
        print(self.__dict__)


object1 = {'id': '8229d5bb-d6be-4cf4-a131-1ef72dbc2b68', 'created_at': '2023-02-12T18:30:20.766624', 'updated_at': '2023-02-12T18:30:20.766624', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
objects2 = {'id': '3627ff02-6b60-40dd-8a24-cc3ee477917d', 'created_at': '2023-02-12T18:39:50.000312', 'updated_at': '2023-02-12T18:39:50.000312', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
#     with open("storage.json", "w") as file:
#         json.dump(dict, file)
filepath = "./storage.json"


def dumper(obj):
    # if os.path.exists(filepath):
    with open(filepath, "w") as file:
        json.dump(obj, file)

def loader():
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            new_object = json.load(file)
            return new_object


def new(object, obj):
    key = f"{obj.__class__.__name__}.{obj.id}"
    object[key] = obj.__dict__

object = {}
testobj = Testcode()
testobj2 = Testcode()
testobj3 = Testcode()
new(object, testobj)
new(object, testobj2)
new(object, testobj3)

print(object)
dumper(object)
new_obj = loader()
print(new_obj)

