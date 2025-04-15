#!/usr/bin/env python3
# lib/debug.py

from models.hiker import Hiker
from models.hike import Hike
from models.__init__ import CURSOR, CONN
import random
import ipdb

def reset_database():
    
    # Reset database tables
    Hiker.drop_table()
    Hike.drop_table()
    Hiker.create_table()
    Hike.create_table()

    # Create 20 Trail instances
    trail_names = ["Sunset Ridge", "Rocky Path", "Pine Valley", "Bear Creek", "Eagle Summit", "Hidden Falls", "Wildflower Trail", "Misty Woods", "Canyon Loop", "Maple Pass", "Silver Lake", "Golden Peak", "Shadow Mountain", "Crystal Springs", "Lone Pine", "Blue Ridge", "Thunder Pass", "Highland Trek", "Serenity Trail", "Redwood Route"]

    # Create 20 Hiker instances
    hiker_names = ["John", "Emily", "Mike", "Sarah", "David", "Laura", "Chris", "Anna", "James", "Sophia", "Daniel", "Olivia", "Matthew", "Emma", "Andrew", "Isabella", "Ryan", "Mia", "Ethan", "Charlotte"]

    [Hiker.create(name, random.randint(18, 65)) for name in hiker_names]

    print("Hikers in memory:", Hiker.all.keys())

    hikers = Hiker.get_all()
    # Create 20 Hike instances, randomly assigning trails and hikers 
    for _ in range(60):
        Hike.create(random.choice(trail_names), random.choice(hikers))

    print("Hikes in DB:", CURSOR.execute("SELECT * FROM hikes").fetchall())
    
reset_database()
ipdb.set_trace()
