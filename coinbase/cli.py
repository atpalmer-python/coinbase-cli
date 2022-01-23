from . import click
from pprint import pprint
from .http import request, noauth_request


# TODO:
# -implement pagination
# -implement endpoint parameters


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
@click.url_argument('user_id')
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
@click.url_argument('account_id')
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
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/addresses'))


# https://developers.coinbase.com/api/v2#show-addresss
@address.command()
@click.url_argument('account_id')
@click.url_argument('address_id')
def show(account_id, address_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/addresses/{address_id}'))


# https://developers.coinbase.com/api/v2#list-address39s-transactions
@address.command()
@click.url_argument('account_id')
@click.url_argument('address_id')
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
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/transactions'))


# https://developers.coinbase.com/api/v2#show-a-transaction
@transaction.command()
@click.url_argument('account_id')
@click.url_argument('transaction_id')
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
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/buys'))


# https://developers.coinbase.com/api/v2#show-a-buy
@buy.command()
@click.url_argument('account_id')
@click.url_argument('buy_id')
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
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/sells'))


# https://developers.coinbase.com/api/v2#show-a-sell
@sell.command()
@click.url_argument('account_id')
@click.url_argument('sell_id')
def show(account_id, sell_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/sells/{sell_id}'))


# TODO (account sell):
# https://developers.coinbase.com/api/v2#place-sell-order
# https://developers.coinbase.com/api/v2#commit-a-sell


# https://developers.coinbase.com/api/v2#deposits
@account.group()
def deposit():
    pass


@deposit.command()
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/deposits'))


@deposit.command()
@click.url_argument('account_id')
@click.url_argument('deposit_id')
def show(account_id, deposit_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/deposits/{deposit_id}'))


# TODO (account deposits):
# https://developers.coinbase.com/api/v2#deposit-funds
# https://developers.coinbase.com/api/v2#commit-a-deposit


# https://developers.coinbase.com/api/v2#withdrawals
@account.group()
def withdrawal():
    pass


@withdrawal.command()
@click.url_argument('account_id')
def list(account_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/withdrawals'))


@withdrawal.command()
@click.url_argument('account_id')
@click.url_argument('withdrawal_id')
def show(account_id, withdrawal_id):
    pprint(request('GET', f'/v2/accounts/{account_id}/withdrawals/{withdrawal_id}'))


# TODO (account withrdawal)
# https://developers.coinbase.com/api/v2#withdraw-funds
# https://developers.coinbase.com/api/v2#commit-a-withdrawal


# https://developers.coinbase.com/api/v2#payment-methods
@main.group()
def paymethod():
    pass


# https://developers.coinbase.com/api/v2#list-payment-methods
@paymethod.command()
def list():
    pprint(request('GET', f'/v2/payment-methods'))


# https://developers.coinbase.com/api/v2#show-a-payment-method
@paymethod.command()
@click.url_argument('paymethod_id')
def show(paymethod_id):
    pprint(request('GET', f'/v2/payment-methods/{paymethod_id}'))


# https://developers.coinbase.com/api/v2#data-endpoints
@main.group()
def data():
    pass


# https://developers.coinbase.com/api/v2#currencies
@data.command()
def currencies():
    pprint(noauth_request('GET', f'/v2/currencies'))


# https://developers.coinbase.com/api/v2#exchange-rates
@data.command()
def xrates():
    pprint(noauth_request('GET', f'/v2/exchange-rates'))


# https://developers.coinbase.com/api/v2#prices
@data.group()
def prices():
    pass


# https://developers.coinbase.com/api/v2#get-buy-price
@prices.command()
@click.url_argument('currency1')
@click.url_argument('currency2')
def buy(currency1, currency2):
    pprint(noauth_request('GET', f'/v2/prices/{currency1}-{currency2}/buy'))


# https://developers.coinbase.com/api/v2#get-sell-price
@prices.command()
@click.url_argument('currency1')
@click.url_argument('currency2')
def sell(currency1, currency2):
    pprint(noauth_request('GET', f'/v2/prices/{currency1}-{currency2}/sell'))


# https://developers.coinbase.com/api/v2#get-spot-price
@prices.command()
@click.url_argument('currency1')
@click.url_argument('currency2')
def spot(currency1, currency2):
    pprint(noauth_request('GET', f'/v2/prices/{currency1}-{currency2}/spot'))


# https://developers.coinbase.com/api/v2#time
@data.command()
def time():
    pprint(noauth_request('GET', f'/v2/time'))

