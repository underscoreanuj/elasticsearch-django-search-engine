from django.urls import path
from .views import home, search


urlpatterns = [
    path('home/', home, name="home"),
    path('home/<slug:index_name>', search, name="upload-file"),
]
