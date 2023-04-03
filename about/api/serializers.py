from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import About


class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['full_name', 'position', 'avatar', 'message']

    def validate(self, attrs):
        full_name = attrs.get('full_name')
        if full_name.islower():
            raise ValidationError({"full_name": "Birinchi harfni bosh harf bilan yozing!"})
        return attrs
