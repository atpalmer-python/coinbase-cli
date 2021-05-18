import hashlib
import hmac
import os
import time
from pprint import pprint

import dotenv
import requests


dotenv.load_dotenv()


def access_sign(ts, method, path, body):
    secret = os.getenv('API_SECRET')
    prehash = ''.join((str(ts), method, path, body))
    return hmac.new(
        secret.encode('utf8'),
        prehash.encode('utf8'),
        hashlib.sha256
    ).hexdigest()


def request(method, path):
    ts = int(time.time())
    response = requests.request(
        method,
        f'https://api.coinbase.com{path}',
        headers={
            'CB-ACCESS-KEY': os.getenv('API_KEY'),
            'CB-ACCESS-SIGN': access_sign(ts, method, path, ''),
            'CB-ACCESS-TIMESTAMP': str(ts),
            'CB-VERSION': '2017-11-26',
        },
    )
    return response.json()


def user():
    return request('GET', '/v2/user')


def user_auth():
    return request('GET', '/v2/user/auth')


def accounts():
    return request('GET', '/v2/accounts')


def account(account_id):
    return request('GET', f'/v2/accounts/{account_id}')


pprint(account('BTC'))

