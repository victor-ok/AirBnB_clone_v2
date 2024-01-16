#!/usr/bin/python3
"""defines a amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    reps a the amenities

    attr:
        name (str): the name of the amenity
    """

    name = ""
