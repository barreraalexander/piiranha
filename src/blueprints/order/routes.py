from flask import Blueprint, request
from src import schemas
from src.config import settings
import requests

router = Blueprint('order_status', __name__, url_prefix='/api')

@router.route('/order_status_update', methods=['POST'])
def order_status():

    try:
        request_json = request.json

        # status_rec = schemas.order_status_update_StatusRec(internalId='cloak')
        # print (status_rec)

        # product_data_update_options = schemas.product_data_update_Options(name='test',pricingIsTotal=1)
        # print(product_data_update_options)
        # res = requests.post(settings.sage_url, json=request_json)

        # order_status_update_request = schemas.order_status_update_Request()


        # data = res.json()
        # return data
        return 'good'

    except Exception as e :
        print (e)
        return 'no json error'
