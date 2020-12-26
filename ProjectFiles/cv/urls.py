from django.urls import path
from .views import about,test

urlpatterns = [
    path('about/', about, name='about'),
    path('test/', test, name='test'),

]
