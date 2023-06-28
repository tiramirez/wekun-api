from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scores import views

urlpatterns = [
    path('images/', views.list_images),
    path('features/<str:file_name>/', views.image_features),
    path('scores/<str:file_name>/', views.image_score),
]

urlpatterns = format_suffix_patterns(urlpatterns)