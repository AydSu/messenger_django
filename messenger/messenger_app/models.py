from statistics import mode
from django.db import models

class Message(models.Model):
    person = models.ForeignKey('Person', on_delete=models.PROTECT, null=True)
    # user_id = models.PositiveIntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Отредактировано')
    read_flag = models.BooleanField(default=False, verbose_name='Прочитано')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True)
    

    def __str__(self):
        return "message" + str(self.id)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Group(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название беседы')

    class Meta:
        verbose_name = 'Беседа'
        verbose_name_plural = 'Беседы'


class Person(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя собеседника')

    class Meta:
        verbose_name = 'Собеседник'
        verbose_name_plural = 'Собеседники'