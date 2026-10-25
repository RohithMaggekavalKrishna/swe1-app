from django.test import TestCase
from django.urls import reverse


class PollsIndexTests(TestCase):
    def test_index_loads(self):
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
