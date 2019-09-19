import couchdb
import os
import bcrypt
ADMIN_USERNAME = 'admin' # Will use the encrypted mode for username and password
ADMIN_PASSWORD = 'root'
COUCHDB_URL = 'http://'+ADMIN_USERNAME+':'+ADMIN_PASSWORD+'@'+os.environ['SERVER_URL']

couch = couchdb.Server(COUCHDB_URL)
class CouchProvider(object):
    def __init__(self):
        self.hashed = bcrypt.hashpw(ADMIN_PASSWORD.encode('utf8'), bcrypt.gensalt())

    def read_product(self, prod_id) -> str:
        db = couch['products']
        if(prod_id in db):
            product = db[prod_id]
            return product, 200
        else:
            return {"error": "Product not found"}, 400
