from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .serializers import PostSerializer, UserSerializer
from blog.models import Post, User

class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# GET list of posts, POST new object to posts
# Authenticated: TRUE
class PostListAPI(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

# GET, PATCH, PUT, DELETE post based on id
# Authenticated: TRUE
class PostDetailAPI(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()