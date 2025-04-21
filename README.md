# Hiker's Trail Tracker CLI App

## Overview

This CLI application allows outdoor enthusiasts and hikers to track their hikes, manage hiker profiles, and log essential hike information. It uses an SQLite database for persistent data storage and is built using Python with an object-oriented approach. This project was developed as part of a Phase 3 assignment at Flatiron School, demonstrating the integration of a command-line interface with object-relational mapping.

---

## Features

- Add, view, update, and delete Hiker profiles
- Log Hikes with name attribute along with the hiker
- View and manage Hikes per Hiker
- SQLite-powered persistent storage
- Clean modular structure separating CLI, helper functions, and data models

---

## File Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py              # CLI main menu interface
    ├── debug.py            # Interactive debugger
    ├── helpers.py          # Reusable helper functions and CLI utilities
    └── models
        ├── __init__.py     # DB setup and initialization
        ├── hiker.py        # Hiker model
        └── hike.py         # Hike model
```

---

## Getting Started

### 1. Install Dependencies

```bash
pipenv install
pipenv shell
```

### 2. Run the CLI

```bash
python lib/cli.py
```

---

## Models

### Hiker (`lib/models/hiker.py`)

Represents an individual hiker.

**Attributes**:
- `id`: Primary key
- `name`: Hiker's name

**Methods**:
- `.create()`
- `.find_by_id()`
- `.update()`
- `.delete()`
- `.all_hikers()`
- `.hikes()` — returns all associated hikes

---

### Hike (`lib/models/hike.py`)

Represents an individual hike entry.

**Attributes**:
- `id`: Primary key
- `name`: Name of the hike
- `hiker_id`: Foreign key linking to a Hiker

**Methods**:
- `.create()`
- `.find_by_id()`
- `.update()`
- `.delete()`
- `.get_by_hiker_id()`
- `.all_hikes()` - unused at this time

---

## CLI (`lib/cli.py`)

The main interactive command-line interface that guides the user through managing hikers and hikes.

**Key options include**:
- View all Hikers
- Add a new Hiker
- Update or Delete a Hiker
- View Hikes for a Hiker
- Add a Hike to a Hiker
- Update or Delete a Hike
- Exit the program

---

## Helpers (`lib/helpers.py`)

Reusable functions that assist with user input and reduce code duplication in `cli.py`.

**Examples**:
- `hikername()`
- `add_hiker()`
- `update_hiker_name()`
- `update_hiker_age()`
- `add_hike()`
- `update_hike()`
- `delete_hike()`

---

## Conclusion

This CLI tool provides a solid foundation for managing hikes and hikers using a simple command-line interface. It can be extended further into a web app or REST API in future phases. Whether you're keeping track of your favorite trails or building out backend CRUD operations, this app gives you full control.

---
