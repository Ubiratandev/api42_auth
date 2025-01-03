from django.urls import path
from .views import test_api
from . import views

urlpatterns = [
    path('test-api/', test_api, name ='test_api'),
    path('cursus/', views.list_cursus, name = "list_cursus" )
]