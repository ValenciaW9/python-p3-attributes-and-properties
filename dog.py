#!/usr/bin/env python3


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Max", "Beagle")
print(dog1.name)  # Output: Max
print(dog1.breed)  # Output: Beagle

dog2 = Dog("Bella", "Labrador")  # This breed is not in the approved list