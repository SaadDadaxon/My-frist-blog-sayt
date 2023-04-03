from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_date']

    def validate(self, attrs):
        name = attrs.get('name')
        if name.islower():
            raise ValidationError({"name": "First letter of name must be uppercase"})
        return attrs
