from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')

        # Replace field items Swith their dict value
        labels = {
            "text" : "Write your thoughts here"
        }

        # Auto apply HTML to field items
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text' : forms.Textarea(attrs={'class': 'form-control my-5'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if 'Happy' not in title:
            raise ValidationError("WHY ARE YOU NOT HAPPY")
        else:
            return title