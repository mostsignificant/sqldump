"""
Library for dumping different file formats directly into a SQL database.
"""

__version__ = '0.0.1'

import json
import os
import pandas as pd
from sqlalchemy import create_engine, engine

def dump_to_sql(filepath: str, sql_connection: str):
    """
    Dumps the given file into the database from the sql connection string.
    """
    if not os.path.isfile(filepath):
        raise Exception(f'file \'{filepath}\' does not exist!')

    engine = create_engine(sql_connection)

    _, extension = os.path.splitext(filepath)

    if extension == '.csv':
        dump_csv_to_sql(filepath, engine)
    elif extension == '.json':
        dump_json_to_sql(filepath, engine)
    elif extension == '.xml':
        dump_xml_to_sql(filepath, engine)
    else:
        raise Exception(f'file extension \'{extension}\' is not supported!')

def dump_csv_to_sql(filepath: str, engine: engine.Engine):
    """
    Dumps the given CSV file into the database from the sql connection string.
    """
    basename = os.path.basename(filepath)
    table = os.path.splitext(basename)[0]

    data = pd.read_csv(filepath)
    data.to_sql(table, engine, if_exists='append')

def dump_json_to_sql(filepath: str, engine: engine.Engine):
    """
    Dumps the given JSON file into the database from the sql connection string.
    """
    basename = os.path.basename(filepath)
    table = os.path.splitext(basename)[0]

    with open(filepath, 'r') as file:
        data = json.loads(file.read())
        data = pd.json_normalize(data)
        data.to_sql(table, engine, if_exists='append')

def dump_xml_to_sql(filepath: str, engine: engine.Engine):
    """
    Dumps the given XML file into the database from the sql connection string.
    """
    basename = os.path.basename(filepath)
    table = os.path.splitext(basename)[0]

    data = pd.read_xml(filepath)
    data.to_sql(table, engine, if_exists='append')