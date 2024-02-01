#!/usr/bin/env python3

class Person:
    approved_jobs = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management", 
        "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")