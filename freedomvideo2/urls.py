from django.contrib import admin
from django.urls import path
from video.views import HomeView, NewVideo, LoginView, RegisterView, VideoView, LogoutView, CommentView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('video/<int:pk>', VideoView.as_view(), name='video-detail'),
    path('comment', CommentView.as_view()),
    # path('logout', LogoutView.as_view(), name='logout'),
]

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
