import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client

from flask import Flask, jsonify

import os

app = Flask(__name__)

# store db host/key in environment variables
HOST = os.environ['COSMOSDB_HOST']
MASTER_KEY = os.environ['COSMOSDB_KEY']
DATABASE_ID = 'stackoverflow'
COLLECTION_ID = 'results'

client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY} )
collection_link = f'dbs/{DATABASE_ID}/colls/{COLLECTION_ID}'

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/api/data')
def get_data():
  query = {'query': "SELECT * FROM c WHERE c.id = 'languages'"}
  result = client.QueryDocuments(collection_link, query)
  return jsonify(next(iter(result)))

if __name__ == '__main__':
  app.run()
