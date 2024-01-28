#!/usr/bin/env python3
from dog import Dog
from person import Person
import io
import sys


class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog(name="Fido")
        assert (isinstance(fido, Dog))

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Dog(name="")
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Dog(name=123)
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        assert (fido.name == "Fido")

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Dog(breed="Human")
        except ValueError as e:
            assert str(e) == "Breed must be in the list of approved breeds."
        sys.stdout = sys.__stdout__

    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(breed="Pug")
        assert (fido.breed == "Pug")


class TestPerson:
    '''Person in person.py'''

    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Person(name="")
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Person(name=123)
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Person(
                name="What do people do on their day off? Can't lie around - that's their job.")
        except ValueError as e:
            assert str(
                e) == "Name must be a string between 1 and 25 characters."
        sys.stdout = sys.__stdout__

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        person = Person(name="Ada")
        assert (person.name == "Ada")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            Person(job="Teacher")
        except ValueError as e:
            assert str(e) == "Job must be in the list of approved jobs."
        sys.stdout = sys.__stdout__

    def test_job_in_list(self):
        '''saves job if in job list.'''
        person = Person(job="Sales")
        assert (person.job == "Sales")
