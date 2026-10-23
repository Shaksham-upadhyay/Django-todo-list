from django.urls import path
from .views import *
urlpatterns = [
    path('', home,name='home'),
    path('update/<id>/',update,name='update'),
    path('delete<id>/',delete,name='delete'),
  
]
