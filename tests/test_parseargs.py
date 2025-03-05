#!/usr/bin/env python3
"""
Unit Tests for the ParseArgs() class
"""
import unittest

from src.classes.parseargs import ParseArgs


class TestParseArgs(unittest.TestCase):
    """
    Unit Tests for the ParseArgs() class
    """

    def setUp(self) -> None:
        self.password = 'Password123'
        self.args = [
            '--password', self.password
        ]
        self.parseargs = ParseArgs(self.args)
        return super().setUp()

    def tearDown(self) -> None:
        del self.parseargs
        del self.args
        del self.password
        return super().tearDown()

    def test_no_arguments(self) -> None:
        """Assert exit when no required arguments are passed"""
        args = []
        with self.assertRaises(SystemExit):
            parseargs = ParseArgs(args)
            self.assertEqual(parseargs.passwords, [])

    def test_required_argument_passed_with_no_data(self) -> None:
        """Assert exit when argument passed with no data"""
        args = ['-p']
        with self.assertRaises(SystemExit):
            parseargs = ParseArgs(args)
            self.assertEqual(parseargs.passwords, [])

    def test_print_version(self) -> None:
        """Assert exit when version is printed"""
        args = ['-v']
        with self.assertRaises(SystemExit):
            parseargs = ParseArgs(args)
            self.assertEqual(parseargs.passwords, [])

    def test_valid_arguments_single_password(self) -> None:
        """Assert all is working when a single password is given"""
        self.assertEqual(self.password, self.parseargs.passwords[0])

    def test_valid_arguments_multiple_passwords(self) -> None:
        """Assert all is working when multiple passwords are given"""
        passwords = [
            'Password123',
            'HelloWorld',
            'Password1!'
        ]
        args = ['--password']
        for password in passwords:
            args.append(password)
        parseargs = ParseArgs(args)
        self.assertEqual(passwords, parseargs.passwords)


if __name__ == '__main__':
    unittest.main()
