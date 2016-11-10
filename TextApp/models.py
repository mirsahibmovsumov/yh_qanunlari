from django.db import models
from django.db.models.fields import DateTimeField
import os.path

class Text(models.Model):
    text_title = models.CharField(max_length=150)
    text_name1 = models.CharField(max_length=150)
    text_body = models.TextField()
    audio_title = models.CharField(max_length=100)
    audio_file = models.FileField()
    date_created = models.DateTimeField(null=False)

    def __str__(self):
        return "%s" % self.text_title
