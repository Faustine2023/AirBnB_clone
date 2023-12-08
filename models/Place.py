#!/usr/bin/python3
"""Documentation for The Place class"""

from models.base_model import BaseModel





class Place(BaseModel):
    """Defines the Place class"""
    name = ""
    user_id
    city_id =""
    description = ""
    price_night = 0
    number_rooms = 0
    max_no_guests = 0
    altitude = 0
    amenity_ids = []
    no_bathrooms = 0
