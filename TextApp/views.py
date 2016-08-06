from django.shortcuts import render

from rest_framework import viewsets
from .models import Text
from .Serializers import TextSerializer
class TextViewSets(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('-date_created')
    serializer_class = TextSerializer
