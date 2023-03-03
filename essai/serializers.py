from rest_framework import serializers
from .models import*

class VoyageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Voyage
        fields = '__all__'