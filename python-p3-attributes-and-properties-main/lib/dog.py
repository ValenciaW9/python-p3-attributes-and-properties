#!/usr/bin/env python3
class Dog:
    APPROVED_BREEDS = ["Pug", "Labrador", "Golden Retriever"]

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

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
            raise ValueError("Breed must be in the list of approved breeds.")
        self._breed = value
