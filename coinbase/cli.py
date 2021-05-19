import click
from pprint import pprint
from .http import request


# https://developers.coinbase.com/api/v2
@click.group()
def main():
    pass


# https://developers.coinbase.com/api/v2#users
@main.group()
def user():
    pass


# https://developers.coinbase.com/api/v2#show-a-user
@user.command()
@click.argument('user_id')
def show(user_id):
    pprint(request('GET', f'/v2/users/{user_id}'))


# https://developers.coinbase.com/api/v2#show-current-user
@user.command()
def current():
    pprint(request('GET', '/v2/user'))


# https://developers.coinbase.com/api/v2#show-authorization-information
@user.command()
def auth():
    pprint(request('GET', '/v2/user/auth'))


# https://developers.coinbase.com/api/v2#accounts
@main.group()
def account():
    pass


# https://developers.coinbase.com/api/v2#list-accounts
@account.command()
def list():
    pprint(request('GET', '/v2/accounts'))


# https://developers.coinbase.com/api/v2#show-an-account
@account.command()
@click.argument('account_id')
def show(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}'))

