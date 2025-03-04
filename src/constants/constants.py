#!/usr/bin/env python3
"""Constants"""

# argparse
ARGPARSE_PROGRAM_NAME = 'main.py'
ARGPARSE_PROGRAM_DESCRIPTION = 'A program to check if the given password '
ARGPARSE_PROGRAM_DESCRIPTION += 'is part of a known data breach.'
ARGPARSE_VERSION = '0.0.1'
ARGPARSE_AUTHOR = 'Benjamin Owen'
ARGPARSE_REPO = 'https://github.com/benowe1717/password-checker'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'
RETRY_CODES = [
    429,
    500,
    502,
    503,
    504,
]
TIMEOUT = 10
