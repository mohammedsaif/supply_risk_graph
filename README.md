                    ┌──────────────┐
                    │   Country    │
                    └──────▲───────┘
                           │
                       LOCATED_IN
                           │
                    ┌──────┴───────┐
                    │   Supplier   │
                    └──────┬───────┘
                           │
                        SUPPLIES
                           │
                    ┌──────▼───────┐
                    │  Component   │
                    └──────┬───────┘
                           │
                         USED_IN
                           │
                    ┌──────▼───────┐
                    │   Product    │
                    └──────┬───────┘
                           │
                    MANUFACTURED_AT
                           │
                    ┌──────▼───────┐
                    │    Plant     │
                    └──────────────┘


        ┌───────────┐
        │ Shipment  │
        └─────┬─────┘
              │
          CONTAINS
              │
              ▼
         Component

        Shipment
              │
         DESTINED_FOR
              │
              ▼
            Plant




            # Supply Chain Risk Graph with Python and Neo4j

## Overview

This project demonstrates how graph databases can be used to model and analyze supply-chain dependencies.

The application uses Python and Neo4j to create a supply-chain graph containing:

- Suppliers
- Components
- Products
- Plants
- Shipments
- Countries

The graph also models Tier-2 supplier relationships to demonstrate multi-level supply-chain dependency analysis.

---

## Business Problem

Modern supply chains often involve multiple suppliers, components, manufacturing plants, and geographic locations.

A disruption at one supplier can affect:

Supplier → Component → Product → Plant

The problem becomes more complex when a supplier itself depends on another supplier.

For example:

Supplier D
→ Supplier A
→ Component X
→ Product Y
→ Bangalore Plant

A relational database can represent this information, but graph databases are particularly useful when the main question involves relationships and traversal.

This project uses Neo4j to answer supply-chain risk questions through graph traversal.

---

## Technology Stack

- Python
- Neo4j Aura
- Neo4j Python Driver
- Cypher
- python-dotenv
- Git / GitHub

---

## Graph Model

### Nodes

- Supplier
- Component
- Product
- Plant
- Shipment
- Country

### Relationships

```text
Supplier → SUPPLIES → Component

Component → USED_IN → Product

Product → MANUFACTURED_AT → Plant

Supplier → LOCATED_IN → Country

Shipment → CONTAINS → Component

Shipment → DESTINED_FOR → Plant

Supplier → SUPPLIES → Supplier