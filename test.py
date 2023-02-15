# import datetime
# import uuid
# import json
# import os.path


# class Testcode:
#     def __init__(self):
#         self.id = str(uuid.uuid4())
#         self.name = 'Name'
#         self.test = 'correct'
#         print(self.__dict__)


# object1 = {'id': '8229d5bb-d6be-4cf4-a131-1ef72dbc2b68', 'created_at': '2023-02-12T18:30:20.766624', 'updated_at': '2023-02-12T18:30:20.766624', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
# objects2 = {'id': '3627ff02-6b60-40dd-8a24-cc3ee477917d', 'created_at': '2023-02-12T18:39:50.000312', 'updated_at': '2023-02-12T18:39:50.000312', 'name': 'My_First_Model', 'my_number': 89, '__class__': 'BaseModel'}
# #     with open("storage.json", "w") as file:
# #         json.dump(dict, file)
# filepath = "./storage.json"


# def dumper(obj):
#     # if os.path.exists(filepath):
#     with open(filepath, "w") as file:
#         json.dump(obj, file)

# def loader():
#     if os.path.exists(filepath):
#         with open(filepath, "r") as file:
#             new_object = json.load(file)
#             return new_object


# def new(object, obj):
#     key = f"{obj.__class__.__name__}.{obj.id}"
#     object[key] = obj.__dict__

# object = {}
# testobj = Testcode()
# testobj2 = Testcode()
# testobj3 = Testcode()
# new(object, testobj)
# new(object, testobj2)
# new(object, testobj3)

# print(object)
# dumper(object)
# new_obj = loader()
# print(new_obj)
# import json

# objects = {'BaseModel.b06b3374-95a1-46e3-8411-eae193b0c53b': {'id': 'b06b3374-95a1-46e3-8411-eae193b0c53b', 'created_at': datetime.datetime(2023, 2, 13, 0, 14, 18, 426364), 'updated_at': datetime.datetime(2023, 2, 13, 0, 14, 18, 426364), 'name': 'My_First_Model', 'my_number': 89}}
# with open('file.json', "w") as f:
#     json.dump(objects, f)

# from models.engine.file_storage import FileStorage
# from models import storage

# all_objs = storage.all()
# print(all_objs)

# obj = ['base', 'mode']
# print(len(obj))

# class testfile():
#     def __init__(self) -> None:
#         self.var1 = 'var1'
#         self.var2 = 'var2'
#         self.var3 = 'var3'
#         print(str(self.__dict__))
    
#     def __str__(self) -> str:
#         return 'test returned'

# test1 = testfile()
# test2 = testfile()
# test3 = testfile()
# del test1
# print(test1)
# print(test2)
# print(test3)

# from models.user import User

# user1 = User.to_dict()
# print(user1)

import os
print(os.stat("file.json").st_size == 0)