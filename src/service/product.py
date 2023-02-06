from util.db_util import DBUtil

class ProductService():
    
    def __init__(self):
        print("In product Service")
        
    def get_records(self):
        try:
            print("get product list")
            query = "SELECT * from productList"
            cursor = DBUtil().get_cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            cursor.close()
            return records, 200
        except Exception as ex:
            print("Exception occurred :", ex)
            return f"Exception occurred:{ex}", 500