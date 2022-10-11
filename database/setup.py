import sqlite3
from sqlite3 import Error

DATABASE = r'database.db'

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_tables():
    tables = []

    locations_table = """
        CREATE TABLE IF NOT EXISTS locations (
            id integer PRIMARY KEY,
            country text,
            state text,
            county text
        ) 
    """
    tables.append(locations_table)

    follow_ups_table = """
        CREATE TABLE IF NOT EXISTS follow_ups (
            id integer PRIMARY KEY,
            title text,
            content text
        )
    """
    tables.append(follow_ups_table)

    sightings_table = """
        CREATE TABLE IF NOT EXISTS sightings (
            id integer PRIMARY KEY,
            report_id text,
            class text,
            date_submitted text,
            subtitle text,
            year text,
            season text,
            month text,
            date text,
            nearest_town text,
            nearest_road text,
            observed text,
            also_noticed text,
            other_witnesses text,
            other_stories text,
            time_and_conditions text,
            environment text,
            misc text,
            location_id integer NOT NULL,
            follow_up_id integer NOT NULL
        )

    """
    tables.append(sightings_table)

    with create_connection(DATABASE) as conn:
        c = conn.cursor()

        for table in tables:
            c.execute(table)


if __name__ == '__main__':
    create_tables()