#!/usr/bin/env python3
"""
Unit Tests for the Hasher() class
"""
import unittest

from src.classes.hasher import Hasher


class TestHasher(unittest.TestCase):
    """
    Unit Tests for the Hasher() class
    """

    def setUp(self) -> None:
        self.text = 'Password123'
        self.sha1_hash = 'b2e98ad6f6eb8508dd6a14cfa704bad7f05f6fb1'.upper()
        self.prefix = 'b2e98'.upper()
        self.suffix = 'ad6f6eb8508dd6a14cfa704bad7f05f6fb1'.upper()
        return super().setUp()

    def tearDown(self) -> None:
        del self.suffix
        del self.prefix
        del self.sha1_hash
        del self.text
        return super().tearDown()

    def test_hash_returned_is_expected(self) -> None:
        """Assert working"""
        hasher = Hasher(self.text)
        result = hasher.create_hash()
        self.assertTrue(result)
        self.assertEqual(self.sha1_hash, hasher.sha1_hash)
        self.assertEqual(self.prefix, hasher.prefix)
        self.assertEqual(self.suffix, hasher.suffix)


if __name__ == '__main__':
    unittest.main()
