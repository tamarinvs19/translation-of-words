from django import forms

from .models import Mission


class MissionForm(forms.Form):
    lang = forms.CharField(initial='ru / en', label='Language', max_length=2)
    count_of_words = forms.IntegerField(initial='20', label='Count of words')
    #mode = forms.CharField(label='Mode')

