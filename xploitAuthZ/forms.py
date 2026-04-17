from django import forms
from django.core.exceptions import ValidationError
import os
from .models import Todo


def load_abuse_words():
    words = set()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, 'abuse_words.txt')
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    words.add(word)
    return words


ABUSE_WORDS = load_abuse_words()


def check_abuse(text):
    if not text:
        return False
    text_lower = text.lower()
    for word in ABUSE_WORDS:
        if word in text_lower:
            return True
    return False


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title', '')
        description = cleaned_data.get('description', '')

        if check_abuse(title):
            self.add_error('title', 'Title contains inappropriate language.')
        if check_abuse(description):
            self.add_error('description', 'Description contains inappropriate language.')

        return cleaned_data