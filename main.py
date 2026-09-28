"""Entry point: builds the supply-chain graph and runs sample risk queries."""
from src.traversal_queries import *
from src.create_graph import build_graph
from src.database import Neo4jDatabase
from src.queries import (
    get_plants_affected_by_supplier,
    get_products_affected_by_supplier,
    get_shipments_from_supplier,
    get_single_source_components,
    get_upstream_supplier_chain,
)


def main():
    db = Neo4jDatabase()
    try:
        print("Building supply-chain graph...")
        build_graph(db)
        print("Graph built.\n")

        supplier_id = "SUP-D"

        print(f"Products affected if {supplier_id} fails:")
        for row in get_products_affected_by_supplier(db, supplier_id):
            print(f"  {row}")

        print(f"\nUpstream supplier chain for {supplier_id}:")
        for row in get_upstream_supplier_chain(db, supplier_id):
            print(f"  {row}")

        print(f"\nPlants affected if {supplier_id} fails:")
        for row in get_plants_affected_by_supplier(db, supplier_id):
            print(f"  {row}")

        print(f"\nShipments sourced from {supplier_id}:")
        for row in get_shipments_from_supplier(db, supplier_id):
            print(f"  {row}")

        print("\nSingle-source components (single point of failure risk):")
        for row in get_single_source_components(db):
            print(f"  {row}")
    finally:
        db.close()
def display(title, results):

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    for row in results:
        print(row)


display(
    "QUERY 1 - Supplier -> Component",
    query_1_supplier_components()
)

display(
    "QUERY 2 - Component -> Product",
    query_2_component_products()
)

display(
    "QUERY 3 - Product -> Plant",
    query_3_product_plants()
)

display(
    "QUERY 4 - Supplier -> Component -> Product",
    query_4_supplier_products()
)

display(
    "QUERY 5 - Supplier -> Component -> Product -> Plant",
    query_5_supplier_to_plant()
)

display(
    "QUERY 6 - High Risk Suppliers",
    query_6_high_risk_suppliers()
)

display(
    "QUERY 7 - Critical Components",
    query_7_critical_components()
)

display(
    "QUERY 8 - Component <- Supplier",
    query_8_reverse_supplier_lookup()
)

display(
    "QUERY 9 - Plant <- Product",
    query_9_reverse_product_lookup()
)

display(
    "QUERY 10 - Products Per Supplier",
    query_10_supplier_product_count()
)

display(
    "QUERY 11 - Plants Per Component",
    query_11_component_plant_count()
)

display(
    "QUERY 12 - Supplier To Plant Path",
    query_12_supplier_to_plant_path()
)

display(
    "QUERY 13 - Tier-2 Variable Length Traversal",
    query_13_tier2_traversal()
)

display(
    "QUERY 14 - Tier-2 To Product",
    query_14_tier2_to_product()
)

display(
    "QUERY 15 - Tier-2 To Plant",
    query_15_tier2_to_plant()
)


close_database()
if __name__ == "__main__":
    main()
