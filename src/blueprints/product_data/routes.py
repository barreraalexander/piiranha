from flask import Blueprint, request
from src.config import settings
import requests

router = Blueprint('product_data', __name__, url_prefix='/api')

@router.route('/product_data', methods=['POST'])
def product_data():

    try:
        request_json = request.json
        print (request_json)

    except:
        return 'no json error'


    return 'hi'

