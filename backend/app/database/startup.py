"""Database startup utilities for the MVP application."""

from .schema import initialize_database
from .load_demo_database import load_demo_data


def initialize_application_database():
    """Create tables and load demo operational records."""
    initialize_database()
    load_demo_data()
