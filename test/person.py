# import car class here
from car import Car

class Person:

    def __init__(self, name, occupation):
        self._name = name
        self._occupation = occupation
        
    def __str__(self):
        return self.name
        
    @property
    def name(self):
        return self._name
    
    @property
    def occupation(self):
        return self._occupation
    
    @classmethod
    def has_oldest_car(cls):
        oldest = 0
        owner = []
        for car in Car.all():
            if car.year > oldest:
                owner = [car.owner]
            elif car.year == oldest:
                owner.append(car.owner)
        return owner[-1]
    
    def drives_same_make_as_me(self):
        make = [car.make for car in Car.all() if car.owner == self]
        owner = []
        for car in Car.all():
            if car.make in make and car.owner != self:
                owner.append(car.owner)
        return list(set(owner))
    
    @classmethod
    def drives_a(cls, make):
        owner=[]
        for car in Car.all():
            if car.make == make:
                owner.append(car.owner)
        return (owner)
    
    
    
