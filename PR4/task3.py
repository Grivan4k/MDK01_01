from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class Laptop(Device):
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
        self.is_on=False
        self.batary_level=100
    def turn_on(self):
        if not self.is_on:
          return f"Laptop{self.brand} {self.model} is alredy on"  
    def turn_on(self):
        if self.is_on:
            self.is_on = False
            return f"Laptop{self.brand} {self.model} is shutting down... Goodbuy"
        else:
            return f"Laptop{self.brand} {self.model} is alredy off" 
    def check_battery(self):
        return f"Battery level: {self.batary_level}%"
    def __str__(self):
        return f"Laptop: {self.brand} {self.model}"
class Phone(Device):
    def __init__(self):
        self.is_on = True
    def turn_on():
        if not self.is_on:
            self.is_on = True
            return f"Phone is on"
        return"Phone is alredy on"
    def turn_off():
        if not self.is_on:
            self.is_on = False
            return f"Phone is off"
        return"Phone is alredy off"