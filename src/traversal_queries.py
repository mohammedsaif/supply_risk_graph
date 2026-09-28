from src.database import Neo4jDatabase


db = Neo4jDatabase()


# ============================================================
# QUERY 1
# Single-hop: Supplier -> Component
# ============================================================

def query_1_supplier_components():

    query = """
    MATCH (s:Supplier {name: $supplier_name})
          -[:SUPPLIES]->
          (c:Component)

    RETURN
        s.name AS supplier,
        c.name AS component
    """

    return db.execute_query(
        query,
        {"supplier_name": "Supplier A"}
    )


# ============================================================
# QUERY 2
# Single-hop: Component -> Product
# ============================================================

def query_2_component_products():

    query = """
    MATCH (c:Component {name: $component_name})
          -[:USED_IN]->
          (p:Product)

    RETURN
        c.name AS component,
        p.name AS product
    """

    return db.execute_query(
        query,
        {"component_name": "Component X"}
    )


# ============================================================
# QUERY 3
# Single-hop: Product -> Plant
# ============================================================

def query_3_product_plants():

    query = """
    MATCH (p:Product {name: $product_name})
          -[:MANUFACTURED_AT]->
          (plant:Plant)

    RETURN
        p.name AS product,
        plant.name AS plant
    """

    return db.execute_query(
        query,
        {"product_name": "Product Y"}
    )


# ============================================================
# QUERY 4
# Multi-hop:
# Supplier -> Component -> Product
# ============================================================

def query_4_supplier_products():

    query = """
    MATCH (s:Supplier {name: $supplier_name})
          -[:SUPPLIES]->
          (c:Component)
          -[:USED_IN]->
          (p:Product)

    RETURN
        s.name AS supplier,
        c.name AS component,
        p.name AS product
    """

    return db.execute_query(
        query,
        {"supplier_name": "Supplier A"}
    )


# ============================================================
# QUERY 5
# Full traversal:
# Supplier -> Component -> Product -> Plant
# ============================================================

def query_5_supplier_to_plant():

    query = """
    MATCH (s:Supplier {name: $supplier_name})
          -[:SUPPLIES]->
          (c:Component)
          -[:USED_IN]->
          (p:Product)
          -[:MANUFACTURED_AT]->
          (plant:Plant)

    RETURN
        s.name AS supplier,
        c.name AS component,
        p.name AS product,
        plant.name AS plant
    """

    return db.execute_query(
        query,
        {"supplier_name": "Supplier A"}
    )


# ============================================================
# QUERY 6
# Filtering by node property
# ============================================================

def query_6_high_risk_suppliers():

    query = """
    MATCH (s:Supplier)
    WHERE s.risk_level = $risk_level

    RETURN
        s.name AS supplier,
        s.risk_level AS risk_level
    """

    return db.execute_query(
        query,
        {"risk_level": "High"}
    )


# ============================================================
# QUERY 7
# Filtering by component property
# ============================================================

def query_7_critical_components():

    query = """
    MATCH (c:Component)
    WHERE c.criticality = $criticality

    RETURN
        c.name AS component,
        c.criticality AS criticality
    """

    return db.execute_query(
        query,
        {"criticality": "High"}
    )


# ============================================================
# QUERY 8
# Relationship direction
# Component <- SUPPLIES - Supplier
# ============================================================

def query_8_reverse_supplier_lookup():

    query = """
    MATCH (c:Component {name: $component_name})
          <-[:SUPPLIES]-
          (s:Supplier)

    RETURN
        c.name AS component,
        s.name AS supplier
    """

    return db.execute_query(
        query,
        {"component_name": "Component X"}
    )


# ============================================================
# QUERY 9
# Reverse traversal:
# Plant <- MANUFACTURED_AT - Product
# ============================================================

def query_9_reverse_product_lookup():

    query = """
    MATCH (plant:Plant {name: $plant_name})
          <-[:MANUFACTURED_AT]-
          (p:Product)

    RETURN
        plant.name AS plant,
        p.name AS product
    """

    return db.execute_query(
        query,
        {"plant_name": "Bangalore Plant"}
    )


# ============================================================
# QUERY 10
# Aggregation / COUNT
# Count products per supplier
# ============================================================

def query_10_supplier_product_count():

    query = """
    MATCH (s:Supplier)
          -[:SUPPLIES]->
          (c:Component)
          -[:USED_IN]->
          (p:Product)

    RETURN
        s.name AS supplier,
        count(DISTINCT p) AS product_count

    ORDER BY product_count DESC
    """

    return db.execute_query(query)


# ============================================================
# QUERY 11
# Aggregation / COUNT
# Count plants affected by each component
# ============================================================

def query_11_component_plant_count():

    query = """
    MATCH (c:Component)
          -[:USED_IN]->
          (p:Product)
          -[:MANUFACTURED_AT]->
          (plant:Plant)

    RETURN
        c.name AS component,
        count(DISTINCT plant) AS affected_plants

    ORDER BY affected_plants DESC
    """

    return db.execute_query(query)


# ============================================================
# QUERY 12
# Path query
# ============================================================

def query_12_supplier_to_plant_path():

    query = """
    MATCH path =
        (s:Supplier {name: $supplier_name})
        -[:SUPPLIES]->
        (c:Component)
        -[:USED_IN]->
        (p:Product)
        -[:MANUFACTURED_AT]->
        (plant:Plant)

    RETURN path
    """

    return db.execute_query(
        query,
        {
            "supplier_name": "Supplier A"
        }
    )


# ============================================================
# QUERY 13
# Variable-length traversal
# Tier-2 Supplier -> Tier-1 Supplier -> Component
# ============================================================

def query_13_tier2_traversal():

    query = """
    MATCH (s:Supplier {name: $supplier_name})
          -[:SUPPLIES*1..2]->
          (c:Component)

    RETURN
        s.name AS starting_supplier,
        c.name AS component
    """

    return db.execute_query(
        query,
        {
            "supplier_name": "Supplier D"
        }
    )


# ============================================================
# QUERY 14
# Variable-length traversal to Product
# ============================================================

def query_14_tier2_to_product():

    query = """
    MATCH path =
        (s:Supplier {name: $supplier_name})
        -[:SUPPLIES*1..2]->
        (c:Component)
        -[:USED_IN]->
        (p:Product)

    RETURN
        s.name AS supplier,
        c.name AS component,
        p.name AS product,
        length(path) AS hops
    """

    return db.execute_query(
        query,
        {
            "supplier_name": "Supplier D"
        }
    )


# ============================================================
# QUERY 15
# Full Tier-2 dependency path
# ============================================================

def query_15_tier2_to_plant():

    query = """
    MATCH path =
        (s:Supplier {name: $supplier_name})
        -[:SUPPLIES*1..2]->
        (c:Component)
        -[:USED_IN]->
        (p:Product)
        -[:MANUFACTURED_AT]->
        (plant:Plant)

    RETURN
        s.name AS supplier,
        c.name AS component,
        p.name AS product,
        plant.name AS plant,
        length(path) AS hops
    """

    return db.execute_query(
        query,
        {
            "supplier_name": "Supplier D"
        }
    )


# ============================================================
# Close database
# ============================================================

def close_database():
    db.close()