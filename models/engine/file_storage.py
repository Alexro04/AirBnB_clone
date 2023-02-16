#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models import user, amenity, place, city, review, state


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
                        arg = all_objs[key]['__class__']
                        if arg == 'BaseModel':
                            self.__objects[key] = BaseModel(**all_objs[key])
                        elif arg == 'User':
                            self.__objects[key] = user.User(**all_objs[key])
                        elif arg == 'Place':
                            self.__objects[key] = place.Place(**all_objs[key])
                        elif arg == 'City':
                            self.__objects[key] = city.City(**all_objs[key])
                        elif arg == 'State':
                            self.__objects[key] = state.State(**all_objs[key])
                        elif arg == 'Review':
                            self.__objects[key] = review.Review(**all_objs[key])
                        elif arg == 'Amenity':
                            self.__objects[key] = amenity.Amenity(**all_objs[key])
        else:
            return
