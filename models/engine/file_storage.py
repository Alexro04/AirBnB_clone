#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = './file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        json_dict = {}
        with open(self.__file_path, "w") as f:
            for key, value in self.__objects.items():
                json_dict[key] = value.to_dict()
            json.dump(json_dict, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            if not os.stat(self.__file_path).st_size == 0:
                with open(self.__file_path, "r") as file:
                    all_objs = json.load(file)
                    for key in all_objs:
                        self.__objects[key] = BaseModel(**all_objs[key])
        else:
            return
