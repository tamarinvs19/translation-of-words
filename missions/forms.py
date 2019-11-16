from django import forms
from django.utils import timezone

from .models import Mission


class MissionForm(forms.Form):
    DICTIONARY = (\
            ('list_uni', 'list_uni'),\
            ('weather', 'weather'),\
            ('advertising', 'advertising'),\
            ('travelling', 'travelling'),\
            ('lang_and_text', 'language_and_texting'),\
            ('university2', 'university2'),\
            ('university', 'university'),\
            ('IT', 'IT'),\
            ('workbook', 'workbook',),\
            )
    LANG = (('ru', 'en - ru'), ('en', 'ru - en'))
    lang = forms.ChoiceField(widget=forms.Select, choices=LANG, label='Language')
    count_of_words = forms.IntegerField(initial='20', label='Count of words')
    dictionary = forms.ChoiceField(widget=forms.Select, choices=DICTIONARY, label='Dictionary')
    start_time = timezone.now()
    #mode = forms.CharField(label='Mode')

