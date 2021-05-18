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
@click.argument('user_id')
def show(user_id):
    pprint(request('GET', f'/v2/users/{user_id}'))


@user.command()
def current():
    pprint(request('GET', '/v2/user'))


@user.command()
def auth():
    pprint(request('GET', '/v2/user/auth'))


@main.group()
def account():
    pass


@account.command()
def list():
    pprint(request('GET', '/v2/accounts'))


@account.command()
@click.argument('account_id')
def show(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}'))

