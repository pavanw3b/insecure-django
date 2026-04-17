from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo
from .forms import TodoForm, check_abuse


class AbuseWordFilterTestCase(TestCase):
    def test_check_abuse_with_bad_word(self):
        self.assertTrue(check_abuse('you are stupid'))
        self.assertTrue(check_abuse('this is dumb'))
        self.assertTrue(check_abuse('STUPID'))
        self.assertTrue(check_abuse('You suck'))

    def test_check_abuse_with_clean_text(self):
        self.assertFalse(check_abuse('clean title'))
        self.assertFalse(check_abuse('great work'))

    def test_form_valid_clean_text(self):
        form_data = {
            'title': 'Clean task',
            'description': 'Do something',
            'completed': False,
        }
        form = TodoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_abuse_in_title(self):
        form_data = {
            'title': 'this is stupid',
            'description': 'Do something',
            'completed': False,
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Title contains inappropriate language.', form.errors['title'])

    def test_form_invalid_abuse_in_description(self):
        form_data = {
            'title': 'clean task',
            'description': 'you are dumb',
            'completed': False,
        }
        form = TodoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Description contains inappropriate language.', form.errors['description'])