from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from service.product import ProductService

NS = Namespace(
    'products',
    description='Operations related to Product')

parser = reqparse.RequestParser()

parser.add_argument("Title", type=str, required=True, help="Title")
parser.add_argument("Body", type=str, required=True, help="Body")
parser.add_argument("Variant_SKU", type=str, required=True, help="Variant SKU")

PRODUCT_DETAILS = NS.model('Product_Details', 
                           {
                               "Handle": fields.String(required=True, description="Handle Name"),
                               "Title": fields.String(required=True, description="Title Name"),
                               "Body": fields.String(required=True, description="Body Name"),
                               "Vendor": fields.String(required=False, description="Vendor Name"),
                               "Type": fields.String(required=False, description="Type Name"),
                               "Tags": fields.String(required=False, description="Tags Name"),
                               "Option1_Name": fields.String(required=False, description="Option1 Name"),
                               "Option1_Value": fields.String(required=False, description="Option1 Value"),
                               "Option2_Name": fields.String(required=False, description="Option2 Name"),
                               "Option2_Value": fields.String(required=False, description="Option2 Name"),
                               "Option3_Name": fields.String(required=False, description="Option3 Name"),
                               "Option3_Value": fields.String(required=False, description="Option3 Name"),
                               "Variant_SKU": fields.String(required=False, description="Variant SKU"),
                               "Variant_Grams": fields.Integer(required=False, description="Variant Grams"),
                               "Variant_Inventory_Tracker": fields.String(required=False, description="Variant Inventory Tracker"),
                               "Variant_Inventory_Qty": fields.Integer(required=False, description="Variant Inventory Qty"),
                               "Variant_Inventory_Policy": fields.String(required=False, description="Variant Inventory Policy"),
                               "Variant_Fulfillment_Service": fields.String(required=False, description="Variant Fulfillment Service"),
                               "Variant Price": fields.Float(required=False, description="Variant Price"),
                               "Variant_Compare_At_Price": fields.String(required=False, description="Variant Compare At Price"),
                               "Image_Src": fields.String(required=False, description="Image Src")
                           }
)

# SEARCH_DETAILS = NS.model("Search_details", {
#     "Title": fields.String(required=True, description="Title"),
#     "Body": fields.String(required=True, description="Body"),
#     "Variant_SKU": fields.String(required=True, description="Variant SKU")
# })

# List items (GET)
@NS.route('/')
class ProductsCollection(Resource):
    """ Products Collection """
    def get(self):
        """ Returns list of Products """
        return ProductService().get_records()


# List items by Title, Body, SKU(GET) - Body should have wildcard search
@NS.route('/search')
class ProductSearchCollection(Resource):
    """ Product Wildcard Search """
    
    @NS.expect(parser)
    def get(self):
        """ Return Title, Body, and SKU """
        args = parser.parse_args()
        print("Args:", args)
        return ProductService().get_wild_card_search(args)

# Create Item (POST)
@NS.route('/create')
class ProductCreateCollection(Resource):
    """Create a new record in table"""
    @NS.expect(PRODUCT_DETAILS, validate=True)
    def post(self):
        """ Create a new product """
        return ProductService().add_product(request.json)


# Delete item(DELETE)
@NS.route('/<string:handle>')
class ProductDeleteCollection(Resource):
    """Delete single record from table"""
    def delete(self, handle):
        """ Remove the product """
        return ProductService().remove_product(handle)

# Export as CSV(GET)
@NS.route('/items.csv')
class ProductExportAsCsv(Resource):
    """Export Data as csv """
    def get(self):
        """ Return csv file"""
        return ProductService().export_product_csv()
