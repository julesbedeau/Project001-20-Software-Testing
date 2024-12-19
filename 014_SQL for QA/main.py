import pandas as pd
import sqlite3

# Simulate MySQL/PostgreSQL database using SQLite for sample queries
connection = sqlite3.connect(':memory:')
cursor = connection.cursor()

# Create sample tables and data
cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    manufacturing_location TEXT,
    supply_chain_info TEXT,
    impact_score REAL
);
""")

cursor.execute("""
CREATE TABLE supply_chain (
    id INTEGER PRIMARY KEY,
    product_id INTEGER,
    step_name TEXT,
    environmental_impact REAL,
    FOREIGN KEY(product_id) REFERENCES products(id)
);
""")

# Insert sample data into products table
products_data = [
    (1, 'Paper Coffee Cups', 'Disposable cups', 'USA', 'Local transport', 75.5),
    (2, 'Plastic Bags', 'Single-use bags', 'China', 'International shipping', 90.0),
    (3, 'Electric Vehicles', 'Eco-friendly cars', 'Germany', 'Complex supply chain', 50.0)
]

cursor.executemany("""
INSERT INTO products (id, name, description, manufacturing_location, supply_chain_info, impact_score)
VALUES (?, ?, ?, ?, ?, ?);
""", products_data)

# Insert sample data into supply_chain table
supply_chain_data = [
    (1, 1, 'Raw Material Extraction', 20.5),
    (2, 1, 'Manufacturing', 25.0),
    (3, 2, 'Distribution', 40.0),
    (4, 3, 'Battery Production', 30.0)
]

cursor.executemany("""
INSERT INTO supply_chain (id, product_id, step_name, environmental_impact)
VALUES (?, ?, ?, ?);
""", supply_chain_data)

connection.commit()

# Sample SQL Queries for QA Testing
queries = {
    "Validate Impact Score Range": """
        SELECT id, name, impact_score
        FROM products
        WHERE impact_score < 0 OR impact_score > 100;
    """,
    "Check Orphaned Supply Chain Records": """
        SELECT sc.id, sc.step_name
        FROM supply_chain sc
        LEFT JOIN products p ON sc.product_id = p.id
        WHERE p.id IS NULL;
    """,
    "Aggregate Environmental Impact by Product": """
        SELECT p.name, SUM(sc.environmental_impact) AS total_impact
        FROM products p
        JOIN supply_chain sc ON p.id = sc.product_id
        GROUP BY p.name;
    """,
    "Count Products with Missing Descriptions": """
        SELECT COUNT(*) AS missing_descriptions_count
        FROM products
        WHERE description IS NULL OR description = '';
    """
}

# Execute queries and store results in DataFrames
results = {}
for query_name, query in queries.items():
    results[query_name] = pd.read_sql_query(query, connection)

# Export results to Excel
excel_path = "./QA_SQL_Testing_Results.xlsx"
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    for sheet_name, df in results.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

connection.close()
