from django.db import models
from django.contrib.postgres.fields import JSONField


class SlackModel(models.Model):

    EVENT = 0
    COMMAND = 1

    TYPE_CHOICES = ((EVENT, 'Event'), (COMMAND, 'Command'))

    type = models.IntegerField(choices=TYPE_CHOICES)
    data = JSONField()

    def __str__(self):
        return '{} {}'.format(self.get_type_display(), self.data.get('command'))
