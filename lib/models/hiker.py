from models.__init__ import CURSOR, CONN

class Hiker:
    """Represents a hiker who can hike various trails."""

    all = {}

    def __init__(self, name, age, id = None):
        self.id = id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.id}. Hiker: {self.name}, {self.age} years old."
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception("Hiker name must be a string between 1 and 15 characters.")
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 0 < new_age < 130:
            self._age = new_age
        else:
            raise Exception("Hiker age must be between 0 to 130.")

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
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age):
        """Initialize a new Hiker instance and save the object to the database."""
        hiker = cls(name, age)
        hiker.save()
        return hiker

    def update(self):
        """Update the hiker's name in the database to match the object's current state."""
        if self.id is None:
            raise Exception("Hiker must be saved before it can be updated.")

        sql = """
            UPDATE hikers
            SET name = ?,
            age = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()

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

    @classmethod
    def find_by_id(cls, id):
        """Return Hiker object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM hikers
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Hiker object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM hikers
            WHERE name = ?
        """
 
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def hikes(self):
        """Return a list of all hikes completed by this hiker."""
        from models.hike import Hike
        return Hike.get_by_hiker_id(self.id)

    @classmethod
    def all_hikers(cls):
        return cls.all.values()
