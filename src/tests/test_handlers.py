import unittest
from unittest.mock import patch

from starlette.testclient import TestClient

from external_content import Content
from main import get_app


class TestPingEndpoint(unittest.TestCase):
    _client: TestClient

    def setUp(self) -> None:
        app = get_app()
        self._client = TestClient(app)

    @patch("handlers.ContentService")
    def test_return_external_content(self, mock_ContentService):
        # given
        payload = {"url": "http://example.com"}
        expected_content = '{"content":"foobar"}'

        mock_ContentService().get_content.return_value = Content(expected_content)

        # when
        response = self._client.post("/ping", json=payload)

        # then
        self.assertEqual(expected_content, response.json()["payload"])

    def test_return_400_if_payload_url_site_returned_error(self):
        payload = {"url": "h123tp://example.com"}
        expected_content = b'{"content":"foobar"}'

        # when
        response = self._client.post("/ping", json=payload)

        # then
        self.assertEqual(400, response.status_code)


class TestInfoEndpoint(unittest.TestCase):
    _client: TestClient

    def setUp(self) -> None:
        app = get_app()
        self._client = TestClient(app)

    def test_payload_cisco_content(self):
        # given
        expected_content = b'{"receiver":"Cisco is the best!"}'

        # when
        response = self._client.get("/info")

        # when
        self.assertEqual(expected_content, response.content)

    def test_status_code_200(self):
        # given

        # when
        response = self._client.get("/info")

        # when
        self.assertEqual(200, response.status_code)
