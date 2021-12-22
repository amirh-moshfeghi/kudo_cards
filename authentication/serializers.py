from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from authentication.models import Employee


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = Employee
        fields = ('email', 'password', 'department', 'team', 'is_manager')

    def create(self, validated_data):
        user = Employee.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
