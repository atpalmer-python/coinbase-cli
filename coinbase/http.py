import hashlib
import hmac
import time
import requests
from .env import API_KEY, API_SECRET


def access_sign(ts, method, path, body):
    prehash = ''.join((str(ts), method, path, body))
    return hmac.new(
        API_SECRET.encode('utf8'),
        prehash.encode('utf8'),
        hashlib.sha256
    ).hexdigest()


def request(method, path):
    ts = int(time.time())
    response = requests.request(
        method,
        f'https://api.coinbase.com{path}',
        headers={
            'CB-ACCESS-KEY': API_KEY,
            'CB-ACCESS-SIGN': access_sign(ts, method, path, ''),
            'CB-ACCESS-TIMESTAMP': str(ts),
            'CB-VERSION': '2017-11-26',
        },
    )
    return response.json()

