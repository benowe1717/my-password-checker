#!/usr/bin/env python3
"""
ParseArgs() class file
"""
import argparse

from src.constants import constants


class ParseArgs():
    """
    Accept and validate command line parameters
    """
    NAME = constants.ARGPARSE_PROGRAM_NAME
    DESC = constants.ARGPARSE_PROGRAM_DESCRIPTION
    VERSION = constants.ARGPARSE_VERSION
    AUTHOR = constants.ARGPARSE_AUTHOR
    REPO = constants.ARGPARSE_REPO

    def __init__(self, args) -> None:
        self.args = args
        self.passwords = []
        self.parser = argparse.ArgumentParser(
            prog=self.NAME, description=self.DESC)

        self.parser.add_argument(
            '-v',
            '--version',
            action='store_true',
            required=False,
            help='Show this program\'s current version')

        self.parser.add_argument(
            '-p',
            '--passwords',
            nargs='+',
            required=False,
            help='The password or password(s) to check'
        )

        self.parse_args = self.parser.parse_args(args)

        if len(args) == 0:
            self.parser.print_help()
            self.parser.exit()

        if self.parse_args.version:
            self._print_version()
            self.parser.exit()

        self.passwords = self.parse_args.passwords

    def _print_version(self) -> None:
        """
        Print out the warranty and version number of the program.

        :return: None
        :rtype: None
        """
        print(f'{self.NAME} v{self.VERSION}')
        print(
            'This is free software:',
            'you are free to change and redistribute it.')
        print('There is NO WARARNTY, to the extent permitted by law.')
        print(f'Written by {self.AUTHOR}; see below for original code')
        print(f'<{self.REPO}>')
