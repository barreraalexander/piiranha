from flask import Blueprint, request
from src.config import settings
import requests

router = Blueprint('inventory', __name__, url_prefix='/api')

@router.route('/inventory_update', methods=['POST'])
def product_data():
    service_id = 502
    api_ver = 120
    auth = {
        "acctId" : settings.sage_acct,
        "key": settings.sage_key
    }


    try:
        request_json = request.json

        res = requests.post(settings.sage_url, json=request_json)

        data = res.json()
        return data

    except Exception as e :
        print (e)
        return 'no json error'
