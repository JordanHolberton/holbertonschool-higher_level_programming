#!/usr/bin/env python3
"""Create class animal"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for Animals"""

    @abstractmethod
    def sound(self):
        """Abstract method for sound"""
        pass


class Dog(Animal):
    """Subclass of Animal for Dog"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Subclass of Animal for Cat"""

    def sound(self):
        return "Meow"
