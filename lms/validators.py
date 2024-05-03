import re
from rest_framework import serializers


class URLValidator:
    '''Класс валидации ссылки.'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''Функция проверки допустимой ссылки.'''
        value = value.get(self.field)
        if value is None:
            return
        if not re.match(r'^https?://(www\.)?youtube\.com/', value):
            raise serializers.ValidationError("Ошибка валидации, ссылка возможна только на сайт 'youtube.com'")