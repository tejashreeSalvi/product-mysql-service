import mysql.connector
from settings import DB_PASSWORD, DB_USER, DB_NAME
import json
import csv
from flask import make_response
from io import StringIO

class DBUtil:
    """ Handle Database operations"""
    
    def __init__(self, db_name = "productList"):
        self.cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD, database=DB_NAME)
        print("Connection:", self.cnx)
        
    def get_all_records(self):
        ''' Fetch all records from mysql'''
        try:
            cursor = self.cnx.cursor()
            query = f"SELECT * FROM productList;"
            cursor.execute(query)
            records = cursor.fetchall()

            row_headers=[x[0] for x in cursor.description]
            json_data = []
            for result in records:
                json_data.append(dict(zip(row_headers, result)))
            print("Records:", records)
            return {"items" :json.dumps(json_data)}, 200
        except Exception as ex:
            print("Exception occurred while fetching all records:", ex)
            return {"error": f"Exception occurred: {ex}"}, 500
    
    def get_wild_card_records(self, data):
        try:
            cursor = self.cnx.cursor()
            title = data['Title']
            body = data['Body']
            sku = data['Variant_SKU']

            query = f"SELECT * FROM productList WHERE Title='{title}' AND Body LIKE '%{body}%' AND Variant_SKU='{sku}'"
            print("query:", query)
            cursor.execute(query)
            records = cursor.fetchall()
            print("Records:", records)
            row_headers = [x[0] for x in cursor.description]
            json_data = []
            for result in records:
                json_data.append(dict(zip(row_headers, result)))
            print("json data:", json_data)
            return {"items": json.dumps(json_data)}, 200
        except Exception as ex:
            print("Exception occurred while fetching all records:", ex)
            return {"error": f"Exception occurred: {ex}"}, 500

    def create_new(self, data):
        try:
            print("\n\ndata:",data)
            cursor = self.cnx.cursor()
            cursor.execute("DESCRIBE productList")
            columns = [row[0] for row in cursor.fetchall()]
            print("Columns:", columns)
            keys, values = zip(*data.items())
            print("Keys, values:", keys, values)

            query = f"INSERT INTO productList ({', '.join(columns)}) VALUES {values}"
            print("Query: ", query)
            result = cursor.execute(query)
            print("Result:", result)
            if result is None:
                self.cnx.commit()
                return {"message": "Item created successfully."}, 201
            else:
                self.cnx.rollback()
            return {"message": "Failed to create item."}, 500
        except Exception as ex:
            print("Exception occurred while fetching all records:", ex)
            return {"error": f"Exception occurred: {ex}"}, 500


    def delete_record(self, name):
        ''' Fetch all records from mysql'''
        try:
            cursor = self.cnx.cursor()
            query = f"DELETE FROM productList WHERE Handle='{name}'"
            cursor.execute(query)
            self.cnx.commit()
            return {"message": "Records Deleted successfully"}, 200
        except Exception as ex:
            print("Exception occurred while fetching all records:", ex)
            return {"error": f"Exception occurred: {ex}"}, 500


    def export_csv(self):

        query = "SELECT Title, Body, Tags From productList"
        cursor = self.cnx.cursor()
        cursor.execute(query)

        items = cursor.fetchall()

        si = StringIO()
        cw = csv.writer(si)
        cw.writerow(['Tile', 'Body', 'Tags'])
        cw.writerows(items)

        output = make_response(si.getvalue())
        output.headers["Content-Disposition"] = "attachment; filename=products.csv"
        output.headers["Content-type"] = "text/csv"
        return output
