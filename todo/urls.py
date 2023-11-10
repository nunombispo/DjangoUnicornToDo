from django.urls import path
from todo.views import index_view

urlpatterns = [
    path('', index_view, name='index'),
]
