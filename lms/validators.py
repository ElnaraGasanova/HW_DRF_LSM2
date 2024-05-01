from rest_framework.serializers import ValidationError


class URLValidator:
    '''Класс валидации ссылки.'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        '''Функция проверки допустимой ссылки.'''
        tmp_url = dict(value).get(self.field)
        if tmp_url is not None and 'youtube.com' not in tmp_url:
            raise ValidationError("Ошибка валидации, ссылка возможна только на сайт 'youtube.com'")
