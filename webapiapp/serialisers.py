from rest_framework import serializers
from . models import recipe

class reciepSerializer(serializers.ModelSerializer):
    class Meta:
        model = recipe
        fields = '__all__'
