from rest_framework import serializers
from blog.models import Post, User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) > 150:
            raise serializers.ValidationError("Title length is too large, please try again.")
        return value
