from flask import Blueprint, request
from src.config import settings
import requests

router = Blueprint('product_data', __name__, url_prefix='/api')

@router.route('/product_data_update', methods=['POST'])
def product_data():

    try:
        request_json = request.json

        res = requests.post(settings.sage_url, json=request_json)

        data = res.json()
        return data

    except Exception as e :
        print (e)
        return 'no json error'
