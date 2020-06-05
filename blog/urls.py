from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('update/<int:blog_id>', views.update, name="update"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
]