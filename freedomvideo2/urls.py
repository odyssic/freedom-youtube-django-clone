from django.contrib import admin
from django.urls import path
from video.views import HomeView, NewVideo, LoginView, RegisterView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view())
]

from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns