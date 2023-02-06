import mysql.connector
from settings import DB_HOST, DB_PASSWORD, DB_USER, DB_NAME

class DBUtil:
    """ Handle Database operations"""
    
    def __init__(self, db_name = "productList"):
        self.cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, database=DB_NAME)
        
        
    def get_cursor(self):
        """ get the cursor"""
        return self.cnx.cursor()
    
    
    
    
        
        
        