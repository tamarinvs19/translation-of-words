from django.shortcuts import render, get_object_or_404

from django.http import Http404, JsonResponse
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views import generic

from django.utils import timezone

from .models import Mission
from .forms import MissionForm
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import csv
from random import randint

import logging as log
log.basicConfig(
        level='DEBUG',
        # %(asctime)s
        format='%(name)s  %(levelname)s  %(filename)s  %(funcName)s  --> %(message)s',
        filename='./trans.log',
        filemode='w',
        )


def generate_words(mission):
    with open(f'dicts/{mission.dictionary}.csv', 'r') as d:
        r = csv.reader(d)
        dicts = [{'ru': row[0], 'en': row[1], 'answer': ''} for r in rows]
    if len(dicts) < mission.count_of_words:
        list_of_words = dicts + \
                [dicts[randint(0, len(dicts)-1)]
                        for _ in range(mission.count_of_words - len(dicts))]
    else:
        list_of_words = [dicts[randint(0, len(dicts)-1)]
                for _ in range(mission.count_of_words)]
        log.debug(list_of_words)
    mission.words = str(list_of_words)


def menu(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            lang = form.cleaned_data['lang']
            count_of_words = form.cleaned_data['count_of_words']
            dictionary = form.cleaned_data['dictionary']

            mission = Mission.objects.create(lang=lang,
                    count_of_words=count_of_words,
                    dictionary=dictionary,
                    )
            mission.save()
            generate_words(mission)
            mission.save()
            context = {'mission': mission}
            addr = '/missions/' + str(mission.id) + '/'
            # return render(request, 'mission.html', context)
            return HttpResponseRedirect(addr, context)
    else:
        form = MissionForm(
                {'lang': 'ru', 'count_of_words': 20, 'dictionary': 'IT'})

        return render(request, 'menu.html', {'form': form})


def mission(request, pk, **kwargs):
    return render(request, 'mission.html')


def next_word(request, pk, **kwargs):
    if request.method == 'GET':
        mission = Mission.objects.get(id=pk)
        if mission.step >= mission.count_of_words:
            data = {'stop': 1, 'href': '/missions/' +
                    str(mission.id) + '/results/'}
        else:
            word = mission.give_next_word()
            answers = mission.generate_list_of_answeres(5)
            lang = {'ru': 'en', 'en': 'ru'}
            lang = lang[mission.lang]
            data = {'stop': 0, 'word': word[lang], 'answers': answers}
        return JsonResponse(data)
    raise Http404


def check_answer(request, pk, **kwargs):
    if request.method == 'POST':
        answer = request.POST.get('answer', None)
        log.debug(answer)
        mission = get_object_or_404(Mission, pk=pk)
        res = mission.check_answer(answer)
        data = {}
        data['right_answer'] = mission.list_of_words[mission.step][mission.lang]
        data['result'] = 'Your answer is ' + res
        mission.step += 1
        mission.save()
        data['step'] = str(mission.step) + ' of ' + str(mission.count_of_words)
        data['res'] = mission.result
        return JsonResponse(data)
    raise Http404


def return_results_page(request, pk, **kwargs):
    mission = get_object_or_404(Mission, pk=pk)
    mission.finish_time = timezone.now()
    res = mission.result
    percent = round(100 * res / mission.count_of_words, 1)
    return render(request, 'result.html', {'res': res,
        'all': mission.count_of_words,
        'percent': percent,
        'time': mission.finish_time - mission.start_time
        })
