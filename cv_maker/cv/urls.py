# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_cv, name='create_cv'),
    path('view/', views.view_cv, name='view_cv'),  # Ensure this matches the redirect
     path('cv/download/<int:personal_info_id>/', views.download_cv, name='download_cv'),

]
