from django.conf.urls import url
from . import views
from blog.api.views import PostListAPI, PostDetailAPI, UserCreateAPI

urlpatterns = [

    # GET, POST, PATCH, PUT Posts
    url(r'^posts/$', PostListAPI.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]*)$', PostDetailAPI.as_view(), name='post-detail'),

    url('api/signup/', UserCreateAPI.as_view(), name='signup'),
]