from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # Token.objects.create
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('id', 'followers')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmptySerializer(serializers.Serializer):
    pass