from util.db_util import DBUtil

class ProductService():
    
    def __init__(self):
        print("In product Service")
        
    def get_records(self):
        try:
            print("get product list")
            records = DBUtil().get_all_records()
            return records
        except Exception as ex:
            print("Exception occurred :", ex)
            return f"Exception occurred:{ex}", 500

    def get_wild_card_search(self, search_details):
        try:
            print("Details: ", search_details)
            response = DBUtil().get_wild_card_records(search_details)
            return response
        except Exception as ex:
            print("Exception occurred :", ex)
            return f"Exception occurred:{ex}", 500

    def add_product(self, product_details):
        try:
            response = DBUtil().create_new(product_details)
            return response
        except Exception as ex:
            print(f"Exception occurred: {ex}")
            return f"Exception occurred: {ex}", 500

    def remove_product(self, name):
        try:
            response = DBUtil().delete_record(name)
            return response
        except Exception as ex:
            print(f"Exception occurred: {ex}")
            return f"Exception occurred: {ex}", 500

        
    def export_product_csv(self):
        try:
            response = DBUtil().export_csv()
            return response
        except Exception as ex:
            print(f"Exception occurred: {ex}")
            return f"Exception occurred: {ex}", 500
