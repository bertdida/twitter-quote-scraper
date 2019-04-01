import re
import functools

ALPHANUM_RE = re.compile(r'[^a-z0-9]')


def to_lowercased_alphanum(text):

    return ALPHANUM_RE.sub('', text.lower())


def compose(*functions):

    def _compose(f, g):

        return lambda arg: g(f(arg))

    return functools.reduce(_compose, functions, lambda arg: arg)
