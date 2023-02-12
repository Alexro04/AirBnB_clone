#!/usr/bin/python3
import json
import os.path


class FileStorage:
    __file_path = './file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj.__dict__

    def save(self):
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects, file)

    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
            # return self.__objects
