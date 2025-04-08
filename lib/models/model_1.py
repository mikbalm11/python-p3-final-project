from models.__init__ import CURSOR, CONN

class Trail:
    
    all = {}
    
    def __init__(self, name, id = None):
        self.id = id
        self.name = name
        # Trail.all.append(self)
    
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
            raise Exception("Trail name must be a string longer than 3 characters.")
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Trail instances """
        sql = """
            CREATE TABLE IF NOT EXISTS trails (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Trail instances """
        sql = """
            DROP TABLE IF EXISTS trails;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Trail object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO trails (name)
                VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        # type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Trail instance and save the object to the database """
        trail = cls(name)
        trail.save()
        return trail

    @classmethod
    def instance_from_db(cls, row):
        """Return an Trail object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        trail = cls.all.get(row[0])
        if trail:
            # ensure attributes match row values in case local instance was modified
            trail.name = row[1]
        else:
            # not in dictionary, create new instance and add to dictionary
            trail = cls(row[1])
            trail.id = row[0]
            cls.all[trail.id] = trail
        return trail

    @classmethod
    def get_all(cls):
        """Return a list containing one Trail object per table row"""
        sql = """
            SELECT *
            FROM trails
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
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

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Hike instances """
        sql = """
            CREATE TABLE IF NOT EXISTS hikes (
            id INTEGER PRIMARY KEY,
            trail_id INTEGER,
            hiker_id INTEGER,
            FOREIGN KEY (trail_id) REFERENCES trails(id),
            FOREIGN KEY (hiker_id) REFERENCES hikers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Hike instances """
        sql = """
            DROP TABLE IF EXISTS hikes;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def all_hikes(self):
        return Hike.all
    
class Hiker:
    
    all = {}
    
    def __init__(self, name, age, id = None):
        self.id = id
        self.name = name
        self.age = age
        # Hiker.all.append(self)

    def __repr__(self):
        return f"Hiker: {self.name}, {self.age} years old."
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Hiker name must be a string between 1 and 15 characters.")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Hiker instances """
        sql = """
            CREATE TABLE IF NOT EXISTS hikers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Hiker instances """
        sql = """
            DROP TABLE IF EXISTS hikers;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name value of the current Hiker object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO hikers (name, age)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        # type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age):
        """ Initialize a new Trail instance and save the object to the database """
        trail = cls(name, age)
        trail.save()
        return trail


    @classmethod
    def instance_from_db(cls, row):
        """Return a Hiker object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        hiker = cls.all.get(row[0])
        if hiker:
            # ensure attributes match row values in case local instance was modified
            hiker.name = row[1]
            hiker.age = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            hiker = cls(row[1], row[2])
            hiker.id = row[0]
            cls.all[hiker.id] = hiker
        return hiker

    @classmethod
    def get_all(cls):
        """Return a list containing one Hiker object per table row"""
        sql = """
            SELECT *
            FROM hikers
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    def hikes(self):
        return [hike for hike in Hike.all if hike.hiker is self]
    
    def all_hikers(self):
        return Hiker.all