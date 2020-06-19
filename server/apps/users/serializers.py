from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for create/retrieve/list Users"""
    confirm_password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = (
            'username', 'email', 'password', 'confirm_password', 'first_name',
            'last_name',
        )

    def validate(self, attrs):
        """Add password matching validation"""
        validate_password(attrs['password'])
        if attrs.pop('confirm_password') == attrs['password']:
            return super().validate(attrs)
        raise serializers.ValidationError('Password mismatch.')

    def create(self, validated_data):
        """"Create User and set password for him"""
        return User.objects.create_user(**validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for update Users"""
    confirm_password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = (
            'username', 'email', 'password', 'confirm_password', 'first_name',
            'last_name',
        )

    def validate(self, attrs):
        """Add password validation for update case"""
        password = attrs.get('password')
        if password:
            if attrs['confirm_password']:
                validate_password(password)
                if attrs.pop('confirm_password') == password:
                    return super().validate(attrs)
                raise serializers.ValidationError('Password mismatch.')
            raise serializers.ValidationError('Confirm password, please.')
        return super().validate(attrs)

    def update(self, instance, validated_data):
        """"Update User"""
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)
