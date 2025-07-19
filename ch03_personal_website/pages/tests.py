from django.test import SimpleTestCase

# Create your tests here.
"""Write the test"""


class HomepageTest(SimpleTestCase):
    def test_home_page_returns_successful(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class AboutpageTest(SimpleTestCase):
    def test_about_page_returns_successful(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
