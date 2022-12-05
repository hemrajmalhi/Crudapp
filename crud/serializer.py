from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    department = serializers.CharField(max_length=255)
    roll = serializers.IntegerField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.department = validated_data.get('department', instance.department)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.save()
        return instance
