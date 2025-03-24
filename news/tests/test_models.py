from django.test import TestCase
from ..models import News

class NewsModelTest(TestCase):
    def setUp(self):
        self.news = News.objects.create(headline='Test Headline', body='Test Body')

    def test_headline_max_length(self):
        max_length = self.news._meta.get_field('headline').max_length
        self.assertEqual(max_length, 200)

    def test_news_creation(self):
        self.assertEqual(self.news.headline, 'Test Headline')
        self.assertEqual(self.news.body, 'Test Body')
