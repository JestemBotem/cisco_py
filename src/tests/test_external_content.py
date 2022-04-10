import unittest

import responses

from src.external_content import ContentService


class TestContentService(unittest.TestCase):
    @responses.activate
    def test_content_if_site_valid(self):
        # given
        url = "https://example.com"
        site_body = "<html>example site</html>"

        cs = ContentService()
        responses.add(**{
            'method': responses.GET,
            'url': url,
            'body': site_body,
            'status': 200,
            'content_type': 'application/html',
        })

        # when
        site_content = cs.get_content(url)

        # then
        self.assertEqual("<html>example site</html>", site_content.content)

    @responses.activate
    def test_return_null_if_invalid_site(self):
        # given
        url = "https://example.com"
        site_body = "<html>404 site not found</html>"

        cs = ContentService()
        responses.add(**{
            'method': responses.GET,
            'url': url,
            'body': site_body,
            'status': 404,
            'content_type': 'application/html',
        })

        # when
        site_content = cs.get_content(url)

        # then
        self.assertIsNone(site_content.content)

    @responses.activate
    def test_return_null_if_status_not_200(self):
        # given
        url = "https://example.com"
        site_body = "<html>Forbidden</html>"

        cs = ContentService()
        responses.add(**{
            'method': responses.GET,
            'url': url,
            'body': site_body,
            'status': 403,
            'content_type': 'application/html',
        })

        # when
        site_content = cs.get_content(url)

        # then
        self.assertIsNone(site_content.content)
