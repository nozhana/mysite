from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_future_date(self): # FIXED
        """
        was_published_recently() returns False for questions whose pub_date
        is in future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_q = Question(pub_date=time)
        self.assertIs(future_q.was_published_recently(), False,
            'Question is in future!')
