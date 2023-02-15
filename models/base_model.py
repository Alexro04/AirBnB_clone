#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.items().__len__() == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                else:
                    self.__dict__[key] = value
            self.created_at = datetime.datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.datetime.fromisoformat(self.updated_at)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
