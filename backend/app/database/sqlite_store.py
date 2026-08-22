"""SQLite persistence layer for the MVP operational database.

The first version keeps the storage simple while allowing workflows to query
actual persisted records instead of loading Python objects directly.
"""

from pathlib import Path
import sqlite3

from .connection import DB_PATH
from .schema import initialize_database


def get_db_connection():
    initialize_database()
    return sqlite3.connect(DB_PATH)


def fetch_one(query, params=()):
    with get_db_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None


def fetch_all(query, params=()):
    with get_db_connection() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]
