from django import forms

from .models import Mission


class MissionForm(forms.Form):
    DICTIONARY = (\
            ('language_and_texting', 'lang_text'),\
            ('university2', 'university2'),\
            ('university', 'university'),\
            ('IT', 'IT'),\
            ('workbook', 'workbook',),\
            )
    lang = forms.CharField(initial='ru / en', label='Language', max_length=2)
    count_of_words = forms.IntegerField(initial='20', label='Count of words')
    dictionary = forms.ChoiceField(widget=forms.Select, choices=DICTIONARY, label='Dictionary')
    #mode = forms.CharField(label='Mode')

