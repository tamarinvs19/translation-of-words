from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime
from random import randint, shuffle
import csv

import logging as log
log.basicConfig(
    level='DEBUG',
    format='%(name)s  %(levelname)s  %(filename)s  %(funcName)s  --> %(message)s',#  %(asctime)s
    filename='./trans.log',
    filemode='w',
)


class Mission(models.Model):
    #player = models.ForeignKey(User, on_delete=models.CASCADE)
    count_of_words = models.PositiveIntegerField(default=20)
    words = models.TextField(default='[{}]')
    step = models.PositiveIntegerField(default=0)
    result = models.PositiveIntegerField(default=0)
    lang = models.TextField(default='ru')
    mode = models.TextField(default='select')
    start_time = models.DateTimeField('start_time',
            null=True)
    local = models.BooleanField(default=False)

    dictionary = models.TextField(default='university')

    @property
    def list_of_words(self):
        ds = self.words[2:-2].split('}, {')
        ds = [dict([[y[1:-1] for y in x.split(': ')]\
                for x in d.split(', ')]) for d in ds]
        return ds

    def give_next_word(self):
        log.debug(self.step)
        return self.list_of_words[self.step]

    def check_answer(self, answer):
        words = self.list_of_words
        words[self.step]['answer'] = answer
        self.words = str(words)
        if answer in self.list_of_words[self.step][self.lang]:
            self.result += 1
            res = 'true'
        else:
            res = 'false'
        return res

    def generate_list_of_answeres(self, count):
        dicts = []
        answers = []
        answers.append(self.list_of_words[self.step][self.lang])
        with open(f'dicts/{self.dictionary}.csv', 'r') as d:
            r = csv.reader(d)
            dicts += [row[0] if self.lang == 'ru' else row[1] for row in r]

        if not self.local:
            with open('dicts/workbook.csv', 'r') as wb:
                r = csv.reader(wb)
                wb_dicts = [row[0] if self.lang == 'ru' else row[1] \
                        for row in r]
            dicts += wb_dicts

        log.debug(dicts)
        list_of_num = []
        while len(list_of_num) < count:
            n = randint(0, len(dicts)-1)
            while n in list_of_num:
                n = randint(0, len(dicts)-1)
            list_of_num.append(n)

        log.debug(list_of_num)
        for l in list_of_num:
            answers.append(dicts[l])
        a = '<div class="radio-container">'
        shuffle(answers)
        c = count + 1
        temp = '<div class="form-item radio-btn nth-{c}"><input style="display: none;" type="radio" name="answer" id="{word}"><label for="{word}">{word}</label></div>'
        for ans in answers:
            a += temp.format(word=ans, c=c)
        a += '</div>'
        return a
