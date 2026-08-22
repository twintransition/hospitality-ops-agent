"""Database connection placeholder for MVP.

The MVP starts with SQLite for local development. This can later be
switched to PostgreSQL without changing workflow logic.
"""

from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).resolve().parent.parent.parent / "hospitality.db"


def get_connection():
    return sqlite3.connect(DB_PATH)
