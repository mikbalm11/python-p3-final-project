class Trail:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Trail: {self.name}"

class Hike:
    
    def __init__(self, name):
        self.name = name
    
class Hiker:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
