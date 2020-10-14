from django.contrib import admin
from django.urls import path
from image.views import HomeView, NewImage, CommentView, LoginView, RegisterView, ImageView, ImageFileView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_image', NewImage.as_view()),
    path('image/<int:id>', ImageView.as_view(), name='image'),
    path('comment', CommentView.as_view()),
    path('get_image/<file_name>', ImageFileView.as_view()),
    path('logout', LogoutView.as_view(), name='logout')
]

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

