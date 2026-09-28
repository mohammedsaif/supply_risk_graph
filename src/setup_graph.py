from src.database import Neo4jDatabase
db = Neo4jDatabase()

def setup_graph():

    db.execute_query("MATCH (n) DETACH DELETE n")

    query = """
    CREATE
    (india:Country {name: "India"}),
    (china:Country {name: "China"}),
    (germany:Country {name: "Germany"}),

    (supplierA:Supplier {
        name: "Supplier A",
        risk_level: "Medium"
    }),

    (supplierB:Supplier {
        name: "Supplier B",
        risk_level: "High"
    }),

    (supplierC:Supplier {
        name: "Supplier C",
        risk_level: "Low"
    }),

    (supplierD:Supplier {
        name: "Supplier D",
        risk_level: "High"
    }),

    (componentX:Component {
        name: "Component X",
        criticality: "High"
    }),

    (componentY:Component {
        name: "Component Y",
        criticality: "Medium"
    }),

    (componentZ:Component {
        name: "Component Z",
        criticality: "Low"
    }),

    (componentW:Component {
        name: "Component W",
        criticality: "High"
    }),

    (productY:Product {
        name: "Product Y"
    }),

    (productZ:Product {
        name: "Product Z"
    }),

    (productA:Product {
        name: "Product A"
    }),

    (bangalore:Plant {
        name: "Bangalore Plant",
        location: "Bangalore"
    }),

    (pune:Plant {
        name: "Pune Plant",
        location: "Pune"
    }),

    (chennai:Plant {
        name: "Chennai Plant",
        location: "Chennai"
    }),

    (shipment1:Shipment {
        id: "SHIP-001",
        status: "In Transit"
    }),

    (shipment2:Shipment {
        id: "SHIP-002",
        status: "Delivered"
    }),

    (supplierA)-[:SUPPLIES]->(componentX),
    (supplierA)-[:SUPPLIES]->(componentY),

    (supplierB)-[:SUPPLIES]->(componentX),

    (supplierC)-[:SUPPLIES]->(componentZ),

    (supplierD)-[:SUPPLIES]->(componentW),

    // Tier-2 supplier
    (supplierD)-[:SUPPLIES]->(supplierA),

    (componentX)-[:USED_IN]->(productY),
    (componentY)-[:USED_IN]->(productY),
    (componentY)-[:USED_IN]->(productZ),
    (componentZ)-[:USED_IN]->(productZ),
    (componentW)-[:USED_IN]->(productA),

    (productY)-[:MANUFACTURED_AT]->(bangalore),
    (productY)-[:MANUFACTURED_AT]->(pune),
    (productZ)-[:MANUFACTURED_AT]->(chennai),
    (productA)-[:MANUFACTURED_AT]->(bangalore),

    (supplierA)-[:LOCATED_IN]->(india),
    (supplierB)-[:LOCATED_IN]->(china),
    (supplierC)-[:LOCATED_IN]->(india),
    (supplierD)-[:LOCATED_IN]->(germany),

    (shipment1)-[:CONTAINS]->(componentX),
    (shipment2)-[:CONTAINS]->(componentY),

    (shipment1)-[:DESTINED_FOR]->(bangalore),
    (shipment2)-[:DESTINED_FOR]->(pune)

    RETURN "Graph created successfully" AS message
    """

    result = db.execute_query(query)

    print(result)


if __name__ == "__main__":
    setup_graph()
    db.close()