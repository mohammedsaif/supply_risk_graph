"""Application-level supply-chain risk queries.

Thin wrappers around the raw Cypher in queries/supply_chain_queries.py,
executed through a Neo4jDatabase connection.
"""

from queries.supply_chain_queries import (
    PLANTS_AFFECTED_BY_SUPPLIER,
    PRODUCTS_AFFECTED_BY_SUPPLIER,
    SHIPMENTS_FROM_SUPPLIER,
    SINGLE_SOURCE_COMPONENTS,
    SUPPLIERS_BY_COUNTRY,
    UPSTREAM_SUPPLIER_CHAIN,
)


def get_products_affected_by_supplier(db, supplier_id):
    return db.execute_query(PRODUCTS_AFFECTED_BY_SUPPLIER, {"supplier_id": supplier_id})


def get_upstream_supplier_chain(db, supplier_id):
    return db.execute_query(UPSTREAM_SUPPLIER_CHAIN, {"supplier_id": supplier_id})


def get_plants_affected_by_supplier(db, supplier_id):
    return db.execute_query(PLANTS_AFFECTED_BY_SUPPLIER, {"supplier_id": supplier_id})


def get_shipments_from_supplier(db, supplier_id):
    return db.execute_query(SHIPMENTS_FROM_SUPPLIER, {"supplier_id": supplier_id})


def get_suppliers_by_country(db, country_name):
    return db.execute_query(SUPPLIERS_BY_COUNTRY, {"country_name": country_name})


def get_single_source_components(db):
    return db.execute_query(SINGLE_SOURCE_COMPONENTS)
