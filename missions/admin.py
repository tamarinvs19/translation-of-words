from django.contrib import admin
from .views import Mission

class MissionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Words', {'fields': ['count_of_words', 'words']}),
        ('Language', {'fields': ['lang', 'dictionary']}),
        ('Result', {'fields': ['result']}),
        ('Time', {'fields': ['start_time']}),
    ]
    list_display = ('lang', 'count_of_words', 'dictionary', 'start_time')
    list_filter = ['start_time']

admin.site.register(Mission)
