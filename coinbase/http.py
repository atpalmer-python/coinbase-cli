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


def noauth_request(method, path, **kwargs):
    response = requests.request(
        method,
        f'https://api.coinbase.com{path}',
        **kwargs)
    return response.json()


def request(method, path):
    ts = int(time.time())
    headers = {
        'CB-ACCESS-KEY': API_KEY,
        'CB-ACCESS-SIGN': access_sign(ts, method, path, ''),
        'CB-ACCESS-TIMESTAMP': str(ts),
        'CB-VERSION': '2017-11-26',
    }
    return noauth_request(method, path, headers=headers)

