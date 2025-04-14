from models.__init__ import CURSOR, CONN

from models.trail import Trail
from models.hiker import Hiker

class Hike:
    """Represents a hiking event linking a hiker with a trail."""

    all = {}

    def __init__(self, trail, hiker, id=None):
        self.id = id
        self.trail = trail
        self.hiker = hiker

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

    def save(self):
        """ Insert a new row with the name value of the current Hike object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO hikes (trail_id, hiker_id)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.trail.id, self.hiker.id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, trail, hiker):
        """ Initialize a new Hike instance and save the object to the database """
        hike = cls(trail, hiker)
        hike.save()
        return hike

    @classmethod
    def instance_from_db(cls, row):
        """Return a Hike object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        hike_id, trail_id, hiker_id = row
        trail = Trail.all.get(trail_id)
        hiker = Hiker.all.get(hiker_id)

        if not trail:
            raise Exception(f"Trail with ID {trail_id} not found.")
        if not hiker:
            raise Exception(f"Hiker with ID {hiker_id} not found.")

        hike = cls.all.get(hike_id)
        if not hike:
            hike = cls(trail, hiker, id=hike_id)
            cls.all[hike_id] = hike

        return hike

    @classmethod
    def get_all(cls):
        """Return a list containing one Hike object per table row"""
        sql = """
            SELECT *
            FROM hikes
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def all_hikes(cls):
        return cls.all.values()
