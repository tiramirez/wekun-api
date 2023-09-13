from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from scores import views

urlpatterns = [
    path('images-list/', views.list_images),
    path('features/<str:file_name>/', views.image_features),
    path('scores/<int:pk>/', views.image_score),
    path('survey/', views.survey),
]

urlpatterns = format_suffix_patterns(urlpatterns)