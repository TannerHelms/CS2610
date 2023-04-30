from django.urls import path, include

from unitconv import views

urlpatterns = [
    path('convert', views.convert, name="convert"),
]