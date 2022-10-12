import sqlite3
from sqlite3 import Error
from database.functions import parse_reports

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

    sightings_table = """
        CREATE TABLE IF NOT EXISTS sightings (
            id integer primary key autoincrement,
            report_id text,
            class_ text,
            date_submitted text,
            subtitle text,
            year text,
            season text,
            month text,
            date text,
            location_details text,
            nearest_town text,
            nearest_road text,
            observed text,
            also_noticed text,
            other_witnesses text,
            other_stories text,
            time_and_conditions text,
            environment text,
            county txt,
            state txt,
            country txt
        )

    """
    tables.append(sightings_table)

    with create_connection(DATABASE) as conn:
        c = conn.cursor()

        for table in tables:
            c.execute(table)

def insert_table(table: str, data: list):
    """
    Insert a list of table objects into the database
    """
    
    data = list(map(lambda obj: obj.get_data(), data))

    length = len(data[0])

    val_str = ''
    for _ in range(length):
        val_str += '?, ' if _ != length -1 else '?'

    with create_connection(DATABASE) as conn:
        c = conn.cursor()

        c.executemany(f"INSERT INTO {table} VALUES({val_str})", data)
        conn.commit()