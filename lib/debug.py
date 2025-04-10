#!/usr/bin/env python3
# lib/debug.py

import random
from models.__init__ import CONN, CURSOR
from models.model_1 import Trail
from models.model_1 import Hiker
from models.model_1 import Hike
import ipdb

def reset_database():
    
    # Create 20 Trail instances
    trail_names = ["Sunset Ridge", "Rocky Path", "Pine Valley", "Bear Creek", "Eagle Summit", "Hidden Falls", "Wildflower Trail", "Misty Woods", "Canyon Loop", "Maple Pass", "Silver Lake", "Golden Peak", "Shadow Mountain", "Crystal Springs", "Lone Pine", "Blue Ridge", "Thunder Pass", "Highland Trek", "Serenity Trail", "Redwood Route"]

    # Create 20 Hiker instances
    hiker_names = ["John", "Emily", "Mike", "Sarah", "David", "Laura", "Chris", "Anna", "James", "Sophia", "Daniel", "Olivia", "Matthew", "Emma", "Andrew", "Isabella", "Ryan", "Mia", "Ethan", "Charlotte"]

    # Reset database tables
    Trail.drop_table()
    Hiker.drop_table()
    Hike.drop_table()
    Trail.create_table()
    Hiker.create_table()
    Hike.create_table()

    [Trail.create(name) for name in trail_names]
    [Hiker.create(name, random.randint(18, 65)) for name in hiker_names]

    print("Trails in memory:", Trail.all.keys())
    print("Hikers in memory:", Hiker.all.keys())

    # Create 20 Hike instances, randomly assigning trails and hikers 
    [Hike.create(random.choice(Trail.get_all()), random.choice(Hiker.get_all())) for hike in range(30)]

    print("Raw hike rows:", CURSOR.execute("SELECT * FROM hikes").fetchall())
    print("Hikes in DB:", CURSOR.execute("SELECT * FROM hikes").fetchall())
    
reset_database()
ipdb.set_trace()
