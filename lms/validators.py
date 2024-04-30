from rest_framework.serializers import ValidationError


class URLValidator:
    '''Класс валидации ссылки.'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''Функция проверки допустимой ссылки.'''
        if 'youtube.com' not in value:
            raise ValidationError('Ошибка валидации, ссылка возможна только на сайт "youtube.com"')