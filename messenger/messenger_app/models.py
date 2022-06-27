from django.db import models

class Message(models.Model):
    user_id = models.PositiveIntegerField()
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Отредактировано')
    read_flag = models.BooleanField(default=False, verbose_name='Прочитано')

    def __str__(self):
        return "message" + str(self.id)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'