from rest_framework import serializers
from TextApp.models import Text

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ("id", "text_title", "text_body", "text_category", "text_tags", "date_created")