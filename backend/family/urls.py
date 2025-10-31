from django.urls import path
from . import views
urlpatterns = [
    path('', views.PersonListAPIView.as_view(), name='person-list'),
]
