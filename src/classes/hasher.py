#!/usr/bin/env python3
"""
Hasher() class file
"""

import hashlib
import re


class Hasher:
    """
    Hash a given piece of text using the SHA1 hashing algorithm
    """

    SHA1_REGEX = r'^[A-F0-9]{40}'

    def __init__(self, text: str) -> None:
        self.text = text

    @property
    def sha1_hash(self) -> str:
        """
        sha1_hash.getter

        :return: The SHA1 hash
        :rtype: str
        """
        return self._sha1_hash

    @sha1_hash.setter
    def sha1_hash(self, hash_string: str) -> None:
        """
        sha1_hash.setter

        :param hash_string: The SHA1 hash
        :type hash_string: str
        :raise ValueError: If the string is not a valid SHA1 hash string
        :return: None
        :rtype: None
        """
        if re.match(self.SHA1_REGEX, hash_string):
            self._sha1_hash = hash_string.upper()
        else:
            raise ValueError(f'ERROR: {hash_string} is not a valid SHA1 hash!')

    @property
    def prefix(self) -> str:
        """
        prefix.getter

        :return: The first 5 characters of a SHA1 hash
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, hash_string: str) -> None:
        """
        prefix.setter

        :param hash_string: The SHA1 hash
        :type hash_string: str
        :raise ValueError: If the string is not a valid SHA1 hash string
        :return: None
        :rtype: None
        """
        if re.match(self.SHA1_REGEX, hash_string):
            self._prefix = hash_string[:5].upper()
        else:
            raise ValueError(f'ERROR: {hash_string} is not a valid SHA1 hash!')

    @property
    def suffix(self) -> str:
        """
        suffix.getter

        :return: The last 35 characters of a SHA1 hash
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, hash_string: str) -> None:
        """
        suffix.setter

        :param hash_string: The SHA1 hash
        :type hash_string: str
        :raise ValueError: If the string is not a valid SHA1 hash string
        :return: None
        :rtype: None
        """
        if re.match(self.SHA1_REGEX, hash_string):
            self._suffix = hash_string[5:].upper()
        else:
            raise ValueError(f'ERROR: {hash_string} is not a valid SHA1 hash!')

    def create_hash(self) -> bool:
        """
        Create a SHA1 hash from the self.text property

        :return: True if the hash was created successfully, False if not
        :rtype: bool
        """
        m = hashlib.sha1(self.text.encode('utf-8'))
        self.sha1_hash = m.hexdigest().upper()
        self.prefix = self.sha1_hash
        self.suffix = self.sha1_hash
        return True
