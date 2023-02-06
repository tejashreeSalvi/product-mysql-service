from flask import request
from flask_restx import Namespace, Resource, fields
from service.product import ProductService
NS = Namespace(
    'products',
    description='Operations related to Product')


@NS.route('/')
class ProductsCollection(Resource):
    """ Products Collection """

   # @JWT_REQUIRED
    def get(self):
        """ Returns list of PROJECTS """
        return ProductService().get_records()