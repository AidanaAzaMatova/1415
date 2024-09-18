from django.test import TestCase
from .models import News, Comment


class NewsModelTest(TestCase):

    def setUp(self):
        self.news_with_comments = News.objects.create(title="News with comments", content="Some content")
        self.news_without_comments = News.objects.create(title="News without comments", content="Some content")

        Comment.objects.create(news=self.news_with_comments, content="This is a comment")

    def test_has_comments_true(self):
        self.assertTrue(self.news_with_comments.has_comments())

    def test_has_comments_false(self):
        self.assertFalse(self.news_without_comments.has_comments())
