from rest_framework import serializers
from .models import Item,Location, File

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('__all__')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('__all__')


     