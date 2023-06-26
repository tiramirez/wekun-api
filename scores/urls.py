from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scores import views

urlpatterns = [
    path('scores/', views.list_images),
    path('scores/<str:file_name>/', views.image_features),
]

urlpatterns = format_suffix_patterns(urlpatterns)