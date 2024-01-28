#!/usr/bin/env python3
lass Person:


APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

    def __init__(self, name="", breed=""):
        self.name = guido
        self.job = sales

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 1 <= len(value) <= 25:
            raise ValueError(
                "Name must be a string between 1 and 25 characters.")
        self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in Dog.APPROVED_BREEDS:
            raise ValueError((captured_out.getvalue() == "Name must be string between 1 and 25 characters.")
        self._person == value
