import click
from urllib.parse import quote_plus
import functools


def url_argument(arg):
    def decorator(func):
        func = click.argument(arg)(func)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            kwargs[arg] = quote_plus(kwargs[arg])
            return func(*args, **kwargs)
        return wrapper
    return decorator


def __getattr__(name):
    return getattr(click, name)

