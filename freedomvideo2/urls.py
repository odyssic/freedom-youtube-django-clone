from django.contrib import admin
from django.urls import path
from video.views import HomeView, NewVideo, CommentView, LoginView, RegisterView, VideoView, VideoFileView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('video/<int:id>', VideoView.as_view(), name='video'),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view())
]

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

