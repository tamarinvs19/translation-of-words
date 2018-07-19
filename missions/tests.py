import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Mission


class MissionModelTests(TestCase):
    def test_count_of_words(self):
        mission1 = Mission(count_of_words=10)
        mission2 = Mission()
        self.assertIs(mission1.count_of_words, 10)
        self.assertIs(mission2.count_of_words, 20)

    def test_list_of_words(self):
        list_of_words = [{"en":"abc","ru":"абв;где","answer":""},{"en":"abcd","ru":"абвг","answer":""}]
        mission = Mission(words=str(list_of_words), step=0)
        for i in range(len(list_of_words)):
            self.assertDictEqual(mission.list_of_words[i], list_of_words[i])

    def test_step(self):
        mission1 = Mission(step=3)
        mission2 = Mission()
        self.assertEqual(mission1.step, 3)
        self.assertEqual(mission2.step, 0)

    def test_lang(self):
        mission = Mission(lang='ru')
        self.assertEqual(mission.lang, 'ru')

    def test_mode(self):
        mission = Mission(mode='mode1')
        self.assertEqual(mission.mode, 'mode1')

    def test_give_next_word(self):
        list_of_words = [{"en":"abc","ru":"абв;где","answer":""},{"en":"abcd","ru":"абвг","answer":""}]
        mission = Mission(words=str(list_of_words), step=0)
        self.assertEqual(mission.give_next_word(), list_of_words[0])
        self.assertEqual(mission.step, 0)

    def test_check_answer(self):
        list_of_words = [{"en":"abc","ru":"абв;где","answer":""},{"en":"abcd","ru":"абвг","answer":""}]
        mission = Mission(words=str(list_of_words), step=0, lang='ru')
        self.assertEqual(mission.check_answer(answer='абв'), True)
        self.assertEqual(mission.step, 1)
        self.assertEqual(mission.list_of_words[0]['answer'], 'абв')
        self.assertEqual(mission.result, 1)

        mission = Mission(words=str(list_of_words), step=0, lang='ru')
        self.assertEqual(mission.check_answer(answer='fhvb'), False)
        self.assertEqual(mission.step, 1)
        self.assertEqual(mission.list_of_words[0]['answer'], 'fhvb')
        self.assertEqual(mission.result, 0)
