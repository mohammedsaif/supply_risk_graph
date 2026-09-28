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


# Supply Chain Graph Traversal with Python & Neo4j

## Overview

This project focuses specifically on graph traversal using Neo4j and Cypher.

The graph is based on a supply-chain risk scenario containing:

- Suppliers
- Components
- Products
- Plants
- Countries
- Shipments

The primary goal is to demonstrate how connected-data questions can be answered using graph traversal.

---

## Core Traversal

The main business traversal is:

Supplier
↓
Component
↓
Product
↓
Plant

This can be extended to Tier-2 suppliers:

Tier-2 Supplier
↓
Tier-1 Supplier
↓
Component
↓
Product
↓
Plant

---

## Traversal Concepts Demonstrated

This project contains 15 Cypher queries demonstrating:

1. Single-hop relationships
2. Multi-hop relationships
3. Property filtering
4. Relationship direction
5. Reverse traversal
6. Aggregation
7. Counting
8. Path queries
9. Variable-length traversal
10. Tier-2 supplier traversal

---

## Query Summary

| Query | Concept |
|------|---------|
| 1 | Single-hop Supplier → Component |
| 2 | Single-hop Component → Product |
| 3 | Single-hop Product → Plant |
| 4 | Multi-hop Supplier → Product |
| 5 | Full Supplier → Plant traversal |
| 6 | Property filtering |
| 7 | Component property filtering |
| 8 | Reverse relationship |
| 9 | Reverse relationship |
| 10 | Aggregation/counting |
| 11 | Aggregation/counting |
| 12 | Path query |
| 13 | Variable-length traversal |
| 14 | Tier-2 traversal |
| 15 | Tier-2 → Plant traversal |

---

## Why Graph Traversal?

In a relational database, a connected-data question often requires thinking about several tables, foreign keys and JOIN operations.

For example:

Supplier
→ Component
→ Product
→ Plant

could require multiple JOINs.

In a graph database, these relationships are represented directly as edges.

Therefore the question can be expressed naturally as:

```text
Supplier
  ↓
Component
  ↓
Product
  ↓
Plant

MATCH (s:Supplier {name: "Supplier A"})
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


    Supplier D
↓
Supplier A
↓
Component X
↓
Product Y
↓
Bangalore Plant



| Query | Concept                | Traversal                              |
| ----- | ---------------------- | -------------------------------------- |
| 1     | Single-hop             | Supplier → Component                   |
| 2     | Single-hop             | Component → Product                    |
| 3     | Single-hop             | Product → Plant                        |
| 4     | Multi-hop              | Supplier → Component → Product         |
| 5     | Multi-hop              | Supplier → Component → Product → Plant |
| 6     | Property filtering     | Supplier risk level                    |
| 7     | Property filtering     | Component criticality                  |
| 8     | Relationship direction | Component ← Supplier                   |
| 9     | Relationship direction | Plant ← Product                        |
| 10    | Aggregation            | Products per supplier                  |
| 11    | Aggregation            | Plants per component                   |
| 12    | Path query             | Supplier → Plant                       |
| 13    | Variable length        | Tier-2 → Component                     |
| 14    | Variable length        | Tier-2 → Product                       |
| 15    | Variable length        | Tier-2 → Plant                         |
