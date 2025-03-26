from django.test import TestCase
from ..models import Movie

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title='Test Movie', description='Test Description', price=9.99)

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, 'Test Movie')
        self.assertEqual(self.movie.description, 'Test Description')
        self.assertEqual(self.movie.price, 9.99)
