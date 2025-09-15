from django.urls import path
from .views import index_views

urlpatterns = [
    path('hello/', index_views.index, name='index'),
    path('about/', index_views.about, name='about'),
]
