import datetime
import os

from dateutil.parser import isoparse
import psycopg
from psycopg.rows import Row

from base.duck import Duck

POSTGRES_USER = os.getenv('POSTGRES_USER') or 'teaching_de'
POSTGRES_DB = os.getenv('POSTGRES_DB') or 'teaching_de'
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD') or 'teaching_de'
POSTGRES_HOSTNAME = os.getenv('POSTGRES_HOSTNAME') or 'localhost'
POSTGRES_PORT = os.getenv('POSTGRES_PORT') or '5432'


class Repository:

    INSERT_DUCK = """INSERT INTO teach.ducks(name, age, address, favorite_pond, duck_created) VALUES 
    (%s, %s, %s, %s, now())
    returning id
    """

    SELECT_DUCK = """
    SELECT (name, age, address, favorite_pond, duck_created, duck_updated) FROM teach.ducks
    where id = %s
    """

    @classmethod
    async def insert_duck(cls, duck: Duck):
        async with await psycopg.AsyncConnection.connect(f"dbname={POSTGRES_DB} user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={POSTGRES_HOSTNAME} port={POSTGRES_PORT}") as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(cls.INSERT_DUCK, (duck.name, duck.age, duck.address, duck.favorite_pond))
                duck_id = await cursor.fetchone()
                return duck_id[0]

    @classmethod
    async def select_duck(cls, duck_id: int) -> Duck | None:
        async with await psycopg.AsyncConnection.connect(f"dbname={POSTGRES_DB} user={POSTGRES_USER} password={POSTGRES_PASSWORD} host={POSTGRES_HOSTNAME} port={POSTGRES_PORT}") as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(cls.SELECT_DUCK, (duck_id, ))
                row = await cursor.fetchone()
                if row is None:
                    return None
                return cls.row_to_duck(row[0])

    @staticmethod
    def row_to_duck(row: Row) -> Duck:

        return Duck(name=row[0], age=row[1], address=row[2], favorite_pond=row[3],
                    duck_created=isoparse(row[4]),
                    duck_updated=isoparse(row[5] or row[4]))
