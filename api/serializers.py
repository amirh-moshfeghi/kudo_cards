from rest_framework import serializers

from authentication.models import Employee
from .models import Kudo


class KudoSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')
    employee = serializers.SlugRelatedField(slug_field=Employee.USERNAME_FIELD, queryset=Employee.objects.all())

    class Meta:
        model = Kudo
        fields = ('id', 'title', 'department', 'team', 'employee', 'date', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Kudo.objects.all())

    class Meta:
        model = Employee
        fields = ('id', 'username', 'kudos')
