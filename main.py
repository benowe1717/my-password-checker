#!/usr/bin/env python3
"""
A secure password checker using haveibeenpwned.com
"""
import sys

from src.classes.hasher import Hasher
from src.classes.parseargs import ParseArgs
from src.classes.requests_wrapper import RequestsWrapper


def main() -> int:
    """Main program loop"""
    args = sys.argv[1:]
    parseargs = ParseArgs(args)
    base_url = 'https://api.pwnedpasswords.com/range/'

    for password in parseargs.passwords:
        hasher = Hasher(password)
        hasher.create_hash()

        url = base_url + hasher.prefix
        try:
            rw = RequestsWrapper(url)
            rw.headers['Host'] = 'api.pwnedpasswords.com'
            rw.headers['Accept'] = 'text/html'
            del rw.headers['Content-Type']
        except ValueError as e:
            print(e)
            continue
        result = rw.make_request()
        if not result:
            continue

        if rw.response.status_code != 200:
            print(
                rw.response.status_code,
                rw.response.text,
                rw.headers,
                rw.response.headers,
                url,
                rw.response.url)
            continue

        passwords = (line.split(':') for line in rw.response.text.splitlines())
        for suffix, count in passwords:
            if hasher.suffix == suffix:
                print('This password has been breached!')
                print(f'This password has been leaked {count} times!')
                break
    return 0


if __name__ == '__main__':
    RESULT = main()
    if RESULT != 0:
        sys.exit(1)
    sys.exit(0)
