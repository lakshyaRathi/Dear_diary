from django.forms import ModelForm
from .models import Entries


class EntryForm(ModelForm):
    class Meta:
        model = Entries
        fields = ('title', 'text', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input is-medium', 'placeholder': 'Enter a title'})
        self.fields['text'].widget.attrs.update(
            {'class': 'textarea', 'placeholder': 'What\'s on your mind?'})
