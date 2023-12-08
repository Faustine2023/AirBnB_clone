#!/usr/bin/python3
"""Documention Module for the User Class"""
from models.base_models import BaseModel





class User(BaseModel):
    """Defines the User Attributes for User class"""
    firstName = ""
    lastName = ""
    email = ""
