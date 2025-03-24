from flask import Flask
from neo4j import GraphDatabase
import os

app = Flask(__name__)

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "testpassword")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.route('/')
def hello():
    return "UMBRIX Backend Running"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
