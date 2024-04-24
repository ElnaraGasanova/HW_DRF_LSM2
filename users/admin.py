from django.contrib import admin
from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Отображение списка пользователей'''
    list_display = ('pk', 'email', 'city',)
    search_fields = ('email',)


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    '''Отображение списка платежей'''
    list_display = ('user', 'payment_date', 'course_paid', 'lesson_paid', 'amount',)
    search_fields = ('payment_date',)
