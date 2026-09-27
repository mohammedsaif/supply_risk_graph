"""Sample supply-chain data used to seed the Neo4j graph.

Models the scenario described in the README:
Supplier D -> Supplier A -> Component X -> Product Y -> Bangalore Plant
"""

COUNTRIES = [
    {"name": "India"},
    {"name": "USA"},
    {"name": "China"},
    {"name": "Germany"},
    {"name": "Vietnam"},
]

SUPPLIERS = [
    {"id": "SUP-A", "name": "Supplier A", "country": "China"},
    {"id": "SUP-B", "name": "Supplier B", "country": "Vietnam"},
    {"id": "SUP-C", "name": "Supplier C", "country": "Germany"},
    {"id": "SUP-D", "name": "Supplier D", "country": "USA"},
    {"id": "SUP-E", "name": "Supplier E", "country": "India"},
]

# Tier-2 dependencies: a supplier that itself supplies another supplier.
SUPPLIER_SUPPLIER = [
    {"from": "SUP-D", "to": "SUP-A"},
]

COMPONENTS = [
    {"id": "COMP-X", "name": "Component X", "supplier_id": "SUP-A"},
    {"id": "COMP-Y", "name": "Component Y", "supplier_id": "SUP-B"},
    {"id": "COMP-Z", "name": "Component Z", "supplier_id": "SUP-C"},
    {"id": "COMP-W", "name": "Component W", "supplier_id": "SUP-E"},
]

PRODUCTS = [
    {"id": "PROD-Y", "name": "Product Y", "component_ids": ["COMP-X", "COMP-Z"]},
    {"id": "PROD-P2", "name": "Product P2", "component_ids": ["COMP-Y", "COMP-W"]},
]

PLANTS = [
    {"id": "PLANT-BLR", "name": "Bangalore Plant", "country": "India", "product_id": "PROD-Y"},
    {"id": "PLANT-AUS", "name": "Austin Plant", "country": "USA", "product_id": "PROD-P2"},
]

SHIPMENTS = [
    {"id": "SHIP-1", "component_id": "COMP-X", "plant_id": "PLANT-BLR"},
    {"id": "SHIP-2", "component_id": "COMP-Z", "plant_id": "PLANT-BLR"},
    {"id": "SHIP-3", "component_id": "COMP-Y", "plant_id": "PLANT-AUS"},
]
