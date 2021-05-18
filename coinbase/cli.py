import click
from pprint import pprint
from .http import request


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

