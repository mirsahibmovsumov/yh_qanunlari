from rest_framework import serializers
from TextApp.models import Text

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ("id", "text_title", "text_name1", "text_body", "audio_file", "date_created")