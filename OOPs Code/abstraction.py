from abc import ABC, abstractmethod

class parent(ABC):
    def __init__(self):
        print("Parent Class")
    @abstractmethod
    def display(self):
        pass


