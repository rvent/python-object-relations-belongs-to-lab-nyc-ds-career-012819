class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car.all().append(self)
        
    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, val):
        self._make = val
    
    @property
    def model(self):
        return self._model
 
    @model.setter
    def model(self, val):
        self._model = val

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, val):
        self._year = val    
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, val):
        self._owner = val
        
    @classmethod
    def all(cls):
        return cls._all
    
    @classmethod
    def cars_driven_by(cls, occupation):
        owners = []
        for car in cls.all():
            if car.owner.occupation == occupation:
                owners.append(car)
        return owners