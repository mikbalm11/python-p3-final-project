class Trail:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Trail: {self.name}"

class Hike:
    
    def __init__(self, trail, hiker):
        self.trail = trail
        self.hiker = hiker

    def __str__(self):
        return f"Hike: {self.trail} completed by {self.hiker}"
    
class Hiker:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hiker: {self.name}, {self.age} years old"