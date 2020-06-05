from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.album, name="album"),
    path('<int:image_id>', views.detailshot, name="detailshot"),
    path('create/', views.create, name="create"),
    path('delete/<int:image_id>', views.deleteimg, name="deleteimg"),
]