"""Builds the supply-chain graph in Neo4j from the sample dataset."""

from data.sample_data import (
    COMPONENTS,
    COUNTRIES,
    PLANTS,
    PRODUCTS,
    SHIPMENTS,
    SUPPLIER_SUPPLIER,
    SUPPLIERS,
)

CONSTRAINTS = [
    "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Country) REQUIRE c.name IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (s:Supplier) REQUIRE s.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Component) REQUIRE c.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (p:Product) REQUIRE p.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (p:Plant) REQUIRE p.id IS UNIQUE",
    "CREATE CONSTRAINT IF NOT EXISTS FOR (s:Shipment) REQUIRE s.id IS UNIQUE",
]


def create_constraints(db):
    for statement in CONSTRAINTS:
        db.execute_query(statement)


def create_countries(db):
    db.execute_query(
        "UNWIND $rows AS row MERGE (:Country {name: row.name})",
        {"rows": COUNTRIES},
    )


def create_suppliers(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MERGE (s:Supplier {id: row.id})
        SET s.name = row.name
        MERGE (c:Country {name: row.country})
        MERGE (s)-[:LOCATED_IN]->(c)
        """,
        {"rows": SUPPLIERS},
    )


def create_supplier_supplier_links(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MATCH (from:Supplier {id: row.from})
        MATCH (to:Supplier {id: row.to})
        MERGE (from)-[:SUPPLIES]->(to)
        """,
        {"rows": SUPPLIER_SUPPLIER},
    )


def create_components(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MERGE (c:Component {id: row.id})
        SET c.name = row.name
        MERGE (s:Supplier {id: row.supplier_id})
        MERGE (s)-[:SUPPLIES]->(c)
        """,
        {"rows": COMPONENTS},
    )


def create_products(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MERGE (p:Product {id: row.id})
        SET p.name = row.name
        WITH p, row
        UNWIND row.component_ids AS component_id
        MATCH (c:Component {id: component_id})
        MERGE (c)-[:USED_IN]->(p)
        """,
        {"rows": PRODUCTS},
    )


def create_plants(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MERGE (pl:Plant {id: row.id})
        SET pl.name = row.name
        MERGE (co:Country {name: row.country})
        MERGE (pl)-[:LOCATED_IN]->(co)
        WITH pl, row
        MATCH (pr:Product {id: row.product_id})
        MERGE (pr)-[:MANUFACTURED_AT]->(pl)
        """,
        {"rows": PLANTS},
    )


def create_shipments(db):
    db.execute_query(
        """
        UNWIND $rows AS row
        MERGE (sh:Shipment {id: row.id})
        WITH sh, row
        MATCH (c:Component {id: row.component_id})
        MATCH (pl:Plant {id: row.plant_id})
        MERGE (sh)-[:CONTAINS]->(c)
        MERGE (sh)-[:DESTINED_FOR]->(pl)
        """,
        {"rows": SHIPMENTS},
    )


def build_graph(db):
    """Creates constraints and loads the full sample supply-chain graph."""
    create_constraints(db)
    create_countries(db)
    create_suppliers(db)
    create_supplier_supplier_links(db)
    create_components(db)
    create_products(db)
    create_plants(db)
    create_shipments(db)
