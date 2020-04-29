from django.urls import reverse

from django.contrib.auth.models import User

from django.test import TestCase, Client


class RegistrationTestCase(TestCase):
    def setUp(self):
        self.c = Client()
