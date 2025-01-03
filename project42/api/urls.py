from django.urls import path
from . import views


urlpatterns = [
    path('test-api/', views.test_api, name ='test_api'),
    path('cursus/', views.list_cursus, name = "list_cursus" ),
    path('login_status/', views.list_status ,name = "list_status")
]