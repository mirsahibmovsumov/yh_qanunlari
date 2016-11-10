from django.shortcuts import render
from rest_framework import status
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets
from .models import Text
from .Serializers import TextSerializer


class TextViewSets(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('-date_created')
    serializer_class = TextSerializer

@api_view(['GET'])
def text_list(request):
    if request.method == 'GET':
        texts = Text.objects.all()
        serializer = TextSerializer(texts, many=True)
        return Response(serializer.data)

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)