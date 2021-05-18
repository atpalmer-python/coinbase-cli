import hashlib
import hmac
import os
import time
from pprint import pprint

import click
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


@click.group()
def main():
    pass


@main.group()
def user():
    pass


@user.command()
def current():
    pprint(request('GET', '/v2/user'))


@user.command()
def auth():
    pprint(request('GET', '/v2/user/auth'))


@main.group()
def accounts():
    pass


@accounts.command()
def list():
    pprint(request('GET', '/v2/accounts'))


@accounts.command()
@click.argument('account_id')
def account(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}'))


main()

