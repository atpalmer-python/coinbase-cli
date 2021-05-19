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


# TODO (user):
# https://developers.coinbase.com/api/v2#update-current-user


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


# TODO (account):
# https://developers.coinbase.com/api/v2#update-account
# https://developers.coinbase.com/api/v2#delete-account


# https://developers.coinbase.com/api/v2#addresses
@account.group()
def address():
    pass


# https://developers.coinbase.com/api/v2#list-addresses
@address.command()
@click.argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/addresses'))


# https://developers.coinbase.com/api/v2#show-addresss
@address.command()
@click.argument('account_id')
@click.argument('address_id')
def show(account_id, address_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/addresses/{address_id}'))


# https://developers.coinbase.com/api/v2#list-address39s-transactions
@address.command()
@click.argument('account_id')
@click.argument('address_id')
def transactions(account_id, address_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/addresses/{address_id}/transactions'))


# https://developers.coinbase.com/api/v2#create-address
# TODO: Create address


# https://developers.coinbase.com/api/v2#transactions
@account.group()
def transaction():
    pass


# https://developers.coinbase.com/api/v2#list-transactions
@transaction.command()
@click.argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/transactions'))


# https://developers.coinbase.com/api/v2#show-a-transaction
@transaction.command()
@click.argument('account_id')
@click.argument('transaction_id')
def show(account_id, transaction_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/transactions{transaction_id}'))


# TODO (account transactions):
# https://developers.coinbase.com/api/v2#send-money
# https://developers.coinbase.com/api/v2#transfer-money-between-accounts
# https://developers.coinbase.com/api/v2#request-money
# https://developers.coinbase.com/api/v2#complete-request-money
# https://developers.coinbase.com/api/v2#re-send-request-money
# https://developers.coinbase.com/api/v2#cancel-request-money


# https://developers.coinbase.com/api/v2#buys
@account.group()
def buy():
    pass


# https://developers.coinbase.com/api/v2#list-buys
@buy.command()
@click.argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/buys'))


# https://developers.coinbase.com/api/v2#show-a-buy
@buy.command()
@click.argument('account_id')
@click.argument('buy_id')
def show(account_id, buy_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/buys/{buy_id}'))


# TODO (account buy):
# https://developers.coinbase.com/api/v2#place-buy-order
# https://developers.coinbase.com/api/v2#commit-a-buy


# https://developers.coinbase.com/api/v2#sells
@account.group()
def sell():
    pass


# https://developers.coinbase.com/api/v2#list-sells
@sell.command()
@click.argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/sells'))


# https://developers.coinbase.com/api/v2#show-a-sell
@sell.command()
@click.argument('account_id')
@click.argument('sell_id')
def show(account_id, sell_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/sells/{sell_id}'))

