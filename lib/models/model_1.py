class Trail:
    
    all =[]
    
    def __init__(self, name):
        self.name = name
        Trail.all.append(self)
    
    def __repr__(self):
        return f"Trail: {self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 3 <= len(new_name) and not hasattr(self, "name"):
            self._name = new_name
        else:
            raise Exception("Trail name must be a string longer than 3 characters.")\
    
    def hikes(self):
        return [hike for hike in Hike.all if hike.trail is self]

    def hikers(self):
        return list({hike.hiker for hike in self.hikes()})
    
    def all_trails(self):
        return Trail.all

class Hike:
    
    all = []
    
    def __init__(self, trail, hiker):
        self.trail = trail
        self.hiker = hiker
        Hike.all.append(self)

    def __repr__(self):
        return f"Hike: {self.trail} completed by {self.hiker}"

    @property
    def hiker(self):
        return self._hiker
    
    @hiker.setter
    def hiker(self, value):
        if isinstance(value, Hiker):
            self._hiker = value
        else:
            raise Exception("Hiker must be an instance of the Hiker class.")
    
    @property
    def trail(self):
        return self._trail
    
    @trail.setter
    def trail(self, value):
        if isinstance(value, Trail):
            self._trail = value
        else:
            raise Exception("Trail must be an instance of the Trail class.")
    
    def all_hikes(self):
        return Hike.all
    
class Hiker:
    
    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Hiker.all.append(self)

    def __repr__(self):
        return f"Hiker: {self.name}, {self.age} years old"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Hiker name must be a string between 1 and 15 characters.")
    
    def hikes(self):
        return [hike for hike in Hike.all if hike.hiker is self]
    
    def all_hikers(self):
        return Hiker.all