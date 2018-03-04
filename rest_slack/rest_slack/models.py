from django.db import models
from django.contrib.postgres.fields import JSONField


class SlackModel(models.Model):

    """
    Abstract base class for creating Slack data models.
    """

    created_at = models.DateTimeField(auto_now_add=True)

    EVENT = 0
    COMMAND = 1

    TYPE_CHOICES = ((EVENT, 'Event'), (COMMAND, 'Command'))

    type = models.IntegerField(choices=TYPE_CHOICES)
    data = JSONField()


    class Meta:
        abstract = True

    def __str__(self):
        return '{}@{}'.format(self.get_type_display(), self.created_at)
