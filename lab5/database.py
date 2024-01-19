import os
import psycopg2

from settings import settings
        
class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.database_hostname,
            port=settings.database_port,
            database=settings.database_name,
            user=settings.database_username,
            password=settings.database_password
        )
        
        self.cursor = self.conn.cursor()

    def get_entities_1(self) -> list:
        """Return set of all entities"""

        with self.conn:
            self.cursor.execute(
                '''SELECT entity1 FROM islab5.choices'''
            )

        return set(item[0] for item in self.cursor.fetchall())
        
    def filter_by_duration(self, entities: set, duration: str) -> set:
        '''Filter by duration and return the intersection with the given entities set'''

        with self.conn:
            self.cursor.execute(
                "SELECT entity1 FROM islab5.choices WHERE duration = %s",
                (duration,)
            )
            filtered_entities = set(item[0] for item in self.cursor.fetchall())

        return entities.intersection(filtered_entities)
    
    def filter_by_principle(self, entities: set, principle: str) -> set:
        '''Filter by principle, allowing for NULL, and return the intersection with the given entities set'''

        with self.conn:
            self.cursor.execute(
                "SELECT entity1 FROM islab5.choices WHERE principle = %s",
                (principle,)
            )
            filtered_entities = set(item[0] for item in self.cursor.fetchall())

        return entities.intersection(filtered_entities)
    
    def filter_by_using_premade(self, entities: set, using_premade: bool) -> set:
        '''Filter by using_premade, allowing for NULL, and return the intersection with the given entities set'''

        with self.conn:
            self.cursor.execute(
                "SELECT entity1 FROM islab5.choices WHERE using_premade= %s",
                (using_premade,)
            )
            filtered_entities = set(item[0] for item in self.cursor.fetchall())

        return entities.intersection(filtered_entities)


database = Database()
    