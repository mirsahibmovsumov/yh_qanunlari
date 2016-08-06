from django.db import models
from django.db.models.fields import DateTimeField


class Text(models.Model):
    STATUS_CHOISES=(
        (0, 'Müsahibələr'),
        (1, 'Sual-Cavab'),
        (2, 'Məqalələr'),
        (3, 'Tərcümələr'),
        (4, 'Kitablar'),
        (5, 'Çıxışlar'),
        (6, 'Təlimlər'),
    )
    text_title = models.CharField(max_length=150)
    text_body = models.TextField()
    text_category = models.IntegerField(choices=STATUS_CHOISES, default=0)
    text_tags = models.CharField(max_length=40)
    date_created = models.DateTimeField(null=False)

    def __str__(self):
        return "%s" % self.text_title
