from flask_restx import Api
from flask import url_for
from .product import NS as product_ns

AUTHORIZATIONS = {
    'Bearer Auth': {
        'type': 'apiKey',
                'in': 'header',
                'name': 'Authorization'
    }
}

class Custom_API(Api):
    @property
    def specs_url(self):
        '''
        The Swagger specifications absolute url (ie. `swagger.json`)

        :rtype: str
        '''
        return url_for(self.endpoint('specs'), _external=False)

API = Custom_API(
    version='0.1.0',
    title='Product List API',
    description='REST API for Product Listing',
    # security='Bearer Auth',
    # authorizations=AUTHORIZATIONS
    )

API.add_namespace(product_ns)

