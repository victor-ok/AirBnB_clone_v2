#!/usr/bin/python3
"""Defines a BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines the BaseModel of the AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """
        initialize a new BaseModel

        Args:
            *args (any): unused.
            **kwargs (dict): key/value pairs of attributes.
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or 1 == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, tform)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """update the update_at attr with the current datetime"""
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        returns the dict representation of the BaseModel instance.

        includes the key/value pair __class__ representing the class
        name of the object
        """
        baseDict = self.__dict__.copy()
        baseDict["created_at"] = self.created_at.isoformat()
        baseDict["updated_at"] = self.update_at.isoformat()
        baseDict["__class__"] = self.__class__.__name__
        return baseDict

    def __str__(self):
        """returns the print representation of the BaseModel instance."""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)
