from django.urls import path
from . import views
urlpatterns = [
    path('v1/persons/', views.PersonListAPIView.as_view(), name='person-list'),
]
