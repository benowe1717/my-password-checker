#!/usr/bin/env python3
"""
Unit Tests for the RequestsWrapper() class
"""
import random
import string
import unittest

from unittest.mock import Mock, patch
from requests.exceptions import ReadTimeout
from requests.models import HTTPError, Response
from requests.exceptions import ConnectionError

from src.classes.requests_wrapper import RequestsWrapper


class TestRequestsWrapper(unittest.TestCase):
    """
    Unit Tests for the RequestsWrapper() class
    """

    def setUp(self) -> None:
        self.prefix = '21BD1'
        self.host = 'api.pwnedpasswords.com'
        self.uri = f'/range/{self.prefix}'
        self.url = f'https://{self.host}{self.uri}'
        self.rw = RequestsWrapper(self.url)
        del self.rw.headers['Content-Type']
        return super().setUp()

    def tearDown(self) -> None:
        del self.rw
        del self.url
        del self.uri
        del self.host
        del self.prefix
        return super().tearDown()

    def test_invalid_url_random_string(self) -> None:
        """Assert url is invalid when given a random string"""
        choices = [
            string.ascii_letters, string.digits, ['-', '_', ':', '/', '.']
        ]
        characters = [character for choice in choices for character in choice]
        url = ''.join(random.choice(characters) for _ in range(100))
        with self.assertRaises(ValueError):
            RequestsWrapper(url)

    def test_invalid_url_no_https(self) -> None:
        """Assert url is invalid when given an http url"""
        url = 'http://api.pwnedpasswords.com/'
        with self.assertRaises(ValueError):
            RequestsWrapper(url)

    def test_invalid_url_no_scheme(self) -> None:
        """Assert url is invalid when no scheme is given"""
        url = f'{self.host}{self.uri}'
        with self.assertRaises(ValueError):
            RequestsWrapper(url)

    def test_invalid_url_no_endpoint_given(self) -> None:
        """Assert url is invalid when no endpoint is present"""
        url = f'https://{self.host}'
        with self.assertRaises(ValueError):
            RequestsWrapper(url)

    @patch('src.classes.requests_wrapper.requests.Session.send')
    def test_failed_request_httperror(self, mock_requests) -> None:
        """Assert result is false when httperror occurs and cannot be
        overcome"""
        mock_response = Mock()
        mock_response.return_value.status_code = 502
        mock_response.return_value.text = 'Bad gateway'
        mock_requests.side_effect = HTTPError(response=mock_response)
        self.rw.headers['Host'] = self.host
        self.rw.headers['Accept'] = 'text/html'
        result = self.rw.make_request()
        self.assertTrue(mock_requests.called)
        self.assertEqual(result, False)

    @patch('src.classes.requests_wrapper.requests.Session.send')
    def test_failed_request_readtimeout(self, mock_requests) -> None:
        """Assert result is false when readtimeout occurs and cannot be
        overcome"""
        mock_requests.side_effect = ReadTimeout
        self.rw.headers['Host'] = self.host
        self.rw.headers['Accept'] = 'text/html'
        with patch('time.sleep', return_value=None) as mock_time:
            result = self.rw.make_request()
        self.assertTrue(mock_requests.called)
        self.assertEqual(result, False)
        self.assertEqual(10, mock_time.call_count)

    @patch('src.classes.requests_wrapper.requests.Session.send')
    def test_failed_request_connectionerror(self, mock_requests) -> None:
        """Assert result is false when connectionerror occurs and cannot be
        overcome"""
        mock_requests.side_effect = ConnectionError
        self.rw.headers['Host'] = self.host
        self.rw.headers['Accept'] = 'text/html'
        with patch('time.sleep', return_value=None) as mock_time:
            result = self.rw.make_request()
        self.assertTrue(mock_requests.called)
        self.assertEqual(result, False)
        self.assertEqual(10, mock_time.call_count)

    @patch('src.classes.requests_wrapper.requests.Session.send')
    def test_200_response(self, mock_requests) -> None:
        """Assert all is working and the right results are returned"""
        lines = []
        line = '000F6468C6E4D09C0C239A4C2769501B3DD:4543'
        lines.append(line.encode() * 800)
        content = b'\n'.join(lines)
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = content
        mock_requests.return_value = mock_response
        self.rw.headers['Host'] = self.host
        self.rw.headers['Accept'] = 'text/html'
        result = self.rw.make_request()
        self.assertTrue(mock_requests.called)
        self.assertTrue(result)
        self.assertEqual(200, self.rw.response.status_code)
        self.assertEqual(content, self.rw.response.content)


if __name__ == '__main__':
    unittest.main()
