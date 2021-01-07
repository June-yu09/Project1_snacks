from django import forms

from .models import SnacksIntro

class SnacksModelForm(forms.ModelForm):
    class Meta:
        model = SnacksIntro
        fields = [
            'title',
            'description', 
            'image',
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)

        mytitle = self.cleaned_data.get('title')
        if mytitle == None:
            #raise forms.ValidationError('Please put the title')
            self.add_error('title', 'Please put the title')
        return cleaned_data