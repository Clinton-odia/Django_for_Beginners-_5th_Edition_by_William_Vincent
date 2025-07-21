from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="this is a message")

    def test_model_content(self):
        self.assertEqual(self.post.text, "this is a message")

    def test_post_url_exist(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_url_name_available(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_post_template_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "post_list.html")

    def test_post_template_contains(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Message Board Homepage</h1>")
