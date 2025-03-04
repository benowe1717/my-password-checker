#!/usr/bin/env python3
"""
RequestsWrapper() class file
"""

import random
import re
import time

import requests
from requests.auth import HTTPBasicAuth

from src.constants import constants


class RequestsWrapper:
    """
    A wrapper for the `requests` library to standardize handling connection
    errors, timeout errors, and non-200 return codes.
    """

    RETRY_CODES = constants.RETRY_CODES
    TIMEOUT = constants.TIMEOUT
    USER_AGENT = constants.USER_AGENT
    URL_REGEX = r'''^https\:\/\/([\w+\-]+\.)+\w{2,}(\.\w{2,})?\/([\w\-\@]+
    (\.\w{3,}|\/))+[\w\-\@]+(\.\w{3,})?'''

    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {
            'Host': '',
            'Accept': '',
            'Content-Type': '',
            'User-Agent': self.USER_AGENT
        }
        self.response = requests.Response()

    @property
    def url(self) -> str:
        """
        url.getter

        :return: The full URL
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        """
        url.setter

        :param url: A string resembling a URL
        :type url: str
        :raise ValueError: If the string is not in valid URL format
        :return: None
        :rtype: None
        """
        pattern = re.compile(self.URL_REGEX, re.X)
        if not re.match(pattern, url):
            raise ValueError(f'{url} is not a valid URL!')
        self._url = url

    def _wait(self) -> None:
        """
        Wait N number of seconds based on random.randint()

        :return: None
        :rtype: None
        """
        seconds = random.randint(self.TIMEOUT, 60)
        print(f'Trying again in {seconds} seconds...')
        time.sleep(seconds)

    def make_request(
        self,
        method='GET',
        params=None,
        json=None,
        auth=None,
    ) -> bool:
        """
        Make a request using the requests library

        :param method: The HTTP Method to use for the request
        :type method: str
        :param params: A dictionary of URL parameters to use with
        form-encoded requests
        :type params: dict
        :param json: A dictionary to be use with a POST body
        :type json: dict
        :param auth: A username and password for use with HTTPBasicAuth
        :type auth: tuple
        :return: True if the request completes (regardless of success), False
        if the request cannot complete
        :rtype: bool
        """
        retries = 10
        for _ in range(retries):
            try:
                session = requests.Session()
                req = requests.Request(
                    method=method,
                    url=self.url,
                    headers=self.headers
                )

                if params:
                    req.data = params

                if json:
                    req.json = json

                if auth:
                    req.auth = HTTPBasicAuth(auth[0], auth[1])

                prepped = req.prepare()
                self.response = session.send(prepped, timeout=self.TIMEOUT)

                if self.response.status_code in self.RETRY_CODES:
                    msg = 'ERROR: [RequestsWrapper] Received '
                    msg += f'{self.response.status_code} so will retry..'
                    print(msg)
                    self._wait()
                    continue
                return True

            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code
                print(f'ERROR: {status_code} :: {e.response.text}')
                if status_code in self.RETRY_CODES:
                    self._wait()
                    continue

            except requests.exceptions.ReadTimeout:
                print('ERROR: Request timed out!')
                self._wait()
                continue

            except requests.exceptions.ConnectionError:
                print('ERROR: Connection errror!')
                self._wait()
                continue
        return False
