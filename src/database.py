import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()


class Neo4jDatabase:

    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        username = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")

        if uri is None:
            raise ValueError("NEO4J_URI environment variable is required")
        if username is None:
            raise ValueError("NEO4J_USERNAME environment variable is required")
        if password is None:
            raise ValueError("NEO4J_PASSWORD environment variable is required")

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(
                query,
                parameters or {}
            )
            return [record.data() for record in result]