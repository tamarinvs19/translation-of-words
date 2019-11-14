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
            default=timezone.now(), null=True)
    finish_time = models.DateTimeField('finish_time', 
            default=tiezone.now(), null=True)

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
        #self.step += 1
        return res

    def generate_list_of_answeres(self, count):
        answers = []
        answers.append(self.list_of_words[self.step][self.lang])
        with open(f'dicts/{self.dictionary}.csv', 'r') as d:
            r = csv.reader(d)
            dicts = []
            for row in r:
                row = {'ru':row[0], 'en':row[1]}
                dicts.append(row[self.lang])
            list_of_num = [randint(0, len(dicts)-1) for _ in range(count)]
            log.error(list_of_num)
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
