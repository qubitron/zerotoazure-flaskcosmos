import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client

from flask import Flask, jsonify

app = Flask(__name__)

settings = {
    'host': '',
    'master_key': '',
    'database_id': 'Tasks',
    'collection_id': 'Items'
}

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
COLLECTION_ID = settings['collection_id']

client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY} )
collection_link = 'dbs/' + DATABASE_ID + '/colls/{0}'.format(COLLECTION_ID) 

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/api/data')
def get_data():
  # The document name is hard-coded
  query_string = "SELECT * FROM c WHERE c.id = 'languages'"
  query = {'query': query_string}
  document = list(client.QueryDocuments(collection_link, query)).pop()
  return jsonify(document)

if __name__ == '__main__':
  app.run()
