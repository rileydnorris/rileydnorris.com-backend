from django.conf.urls import url, include
from . import views
from rest_framework import routers
from blog.api.views import PostListAPI, PostDetailAPI, UserAPI

router = routers.DefaultRouter()
router.register(r'auth', UserAPI)

urlpatterns = [

    # GET, POST, PATCH, PUT Posts
    url(r'^posts/$', PostListAPI.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]*)$', PostDetailAPI.as_view(), name='post-detail'),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^', include(router.urls)),
]