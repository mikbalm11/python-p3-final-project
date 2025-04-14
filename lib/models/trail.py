from models.__init__ import CURSOR, CONN

class Trail:
    """Represents a trail that can be hiked by hikers."""

    all = {}
    
    def __init__(self, name, id = None):
        self.id = id
        self.name = name
    
    def __repr__(self):
        return f"{self.id}. Trail: {self.name}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3: # and not hasattr(self, "name"):
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
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Trail instance and save the object to the database """
        trail = cls(name)
        trail.save()
        return trail

    def update(self):
        """Update the trail's name in the database to match the object's current state."""
        if self.id is None:
            raise Exception("Trail must be saved before it can be updated.")
        
        sql = """
            UPDATE trails
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

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
            trail = cls(name=row[1], id=row[0])
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
    
    @classmethod
    def find_by_id(cls, id):
        """Return Trail object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM trails
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Trail object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM trails
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def hikes(self):
        """Return a list of all hikes associated with this trail."""
        from models.hike import Hike
        return [hike for hike in Hike.all_hikes() if hike.trail is self]

    def hikers(self):
        """Return a list of unique hikers who have hiked this trail."""
        return list({hike.hiker for hike in self.hikes()})

    @classmethod
    def all_trails(cls):
        return cls.all.values()
