from rest_framework import serializers
from .models import Fruit

class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'created_at')
        model = Fruit