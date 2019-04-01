import re
import functools


def to_lowercased_alphanum(text, ):

    return re.sub(r'[^a-z0-9]', '', text.lower())


def compose(*functions):

    def _compose(f, g):

        return lambda arg: g(f(arg))

    return functools.reduce(_compose, functions, lambda arg: arg)
