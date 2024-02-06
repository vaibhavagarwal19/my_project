from rest_framework import serializers
from app1.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description =serializers.CharField()
    active = serializers.BooleanField(read_only=True)

    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance , validated_data):    # instance carrries old values and validated_data carries new values
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance