from django import forms

from .models import Mission


class MissionForm(forms.Form):
    DICTIONARY = (('workbook', 'workbook',), ('IT', 'IT'))
    lang = forms.CharField(initial='ru / en', label='Language', max_length=2)
    count_of_words = forms.IntegerField(initial='20', label='Count of words')
    dictionary = forms.Select(choices=DICTIONARY)#forms.ChoiceField(widget=forms.Select, choices=DICTIONARY)
    #mode = forms.CharField(label='Mode')

