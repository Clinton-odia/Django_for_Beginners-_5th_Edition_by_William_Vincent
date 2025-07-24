"""Test! Test!! Test!!!"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )
        self.assertTrue(user.username, "testuser")
        self.assertTrue(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupPageTests(TestCase):
    def test_url_exist_at_correct_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def signup_form(self):
        response = self.client.post(
            reverse(
                "signup",
                {
                    "username": "testuser3",
                    "email": "testuser3@example.com",
                    "password": "testpassword",
                },
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser3")
        self.assertEqual(
            get_user_model().objects.all()[0].email, "testuser3@example.com"
        )
