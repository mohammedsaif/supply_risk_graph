"""Entry point: builds the supply-chain graph and runs sample risk queries."""

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


if __name__ == "__main__":
    main()
