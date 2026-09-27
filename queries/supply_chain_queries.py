"""Raw Cypher queries for supply-chain risk analysis.

Each constant is a parameterized Cypher statement. Application code (see
src/queries.py) executes these against the Neo4j database.
"""

# Given a supplier id, find every product that could be affected, following
# Supplier -> Component -> Product, plus any downstream suppliers that
# depend on it (tier-2+ dependencies via Supplier -> SUPPLIES -> Supplier).
PRODUCTS_AFFECTED_BY_SUPPLIER = """
MATCH (root:Supplier {id: $supplier_id})
MATCH (root)-[:SUPPLIES*0..]->(dependent:Supplier)
MATCH (dependent)-[:SUPPLIES]->(comp:Component)-[:USED_IN]->(product:Product)
RETURN DISTINCT dependent.id AS supplier_id,
                dependent.name AS supplier_name,
                comp.id AS component_id,
                comp.name AS component_name,
                product.id AS product_id,
                product.name AS product_name
"""

# Full upstream tier-N dependency chain for a supplier: every supplier that
# feeds into it, directly or indirectly.
UPSTREAM_SUPPLIER_CHAIN = """
MATCH path = (upstream:Supplier)-[:SUPPLIES*1..]->(target:Supplier {id: $supplier_id})
RETURN [n IN nodes(path) | n.id] AS chain
ORDER BY length(path)
"""

# Every plant that would be impacted if a given supplier failed.
PLANTS_AFFECTED_BY_SUPPLIER = """
MATCH (root:Supplier {id: $supplier_id})
MATCH (root)-[:SUPPLIES*0..]->(dependent:Supplier)
MATCH (dependent)-[:SUPPLIES]->(comp:Component)-[:USED_IN]->(product:Product)-[:MANUFACTURED_AT]->(plant:Plant)
RETURN DISTINCT plant.id AS plant_id, plant.name AS plant_name
"""

# All shipments carrying components sourced (directly or via tier-N
# suppliers) from a given supplier.
SHIPMENTS_FROM_SUPPLIER = """
MATCH (root:Supplier {id: $supplier_id})
MATCH (root)-[:SUPPLIES*0..]->(dependent:Supplier)
MATCH (dependent)-[:SUPPLIES]->(comp:Component)<-[:CONTAINS]-(shipment:Shipment)-[:DESTINED_FOR]->(plant:Plant)
RETURN DISTINCT shipment.id AS shipment_id, comp.name AS component_name, plant.name AS plant_name
"""

# Suppliers grouped by country, for exposure-by-geography analysis.
SUPPLIERS_BY_COUNTRY = """
MATCH (s:Supplier)-[:LOCATED_IN]->(c:Country {name: $country_name})
RETURN s.id AS supplier_id, s.name AS supplier_name
"""

# Single points of failure: components sourced from exactly one supplier.
SINGLE_SOURCE_COMPONENTS = """
MATCH (c:Component)<-[:SUPPLIES]-(s:Supplier)
WITH c, collect(s) AS suppliers
WHERE size(suppliers) = 1
RETURN c.id AS component_id, c.name AS component_name, suppliers[0].name AS supplier_name
"""
