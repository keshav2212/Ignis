from django.urls import path
from app import views
urlpatterns = [
    path('',views.dashboard),
    path('create',views.create,name='create'),
]
