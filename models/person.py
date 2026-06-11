from abc import ABC, abstractmethod

class Person(ABC):
    """
    Abstract base class for Person
    """
    def __init__(self, person_id, name, mobile_number, address):
        self.person_id = person_id
        self.name = name
        self.mobile_number = mobile_number
        self.address = address
    
    @abstractmethod
    def display_details(self):
        """Display person details"""
        pass
    
    def update_details(self, name=None, mobile_number=None, address=None):
        """Update person details"""
        if name:
            self.name = name
        if mobile_number:
            self.mobile_number = mobile_number
        if address:
            self.address = address
        return True
    
    def __str__(self):
        return f"Person ID: {self.person_id}, Name: {self.name}, Mobile: {self.mobile_number}, Address: {self.address}"
    
    def __repr__(self):
        return f"Person(id={self.person_id}, name={self.name}, mobile={self.mobile_number})"
