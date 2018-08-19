#-*- coding: utf8 -*-

"""Simple module aiming at demonstrating monkey patching with pytest and
the monkeypatch fixture.

This module implements a function using the random.choice standard library
function. This external dependency will be mocked during the unit tests.
"""

from random import choice

def f(data):
    """Returns a random item from a list."""
    return choice(data)

def main():
    """Main entry point."""
    print(f([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
