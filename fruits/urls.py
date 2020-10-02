from django.urls import path
from .views import FruitsList, FruitDetails

urlpatterns = [
    path('', FruitsList.as_view(), name='fruits'),
    path('<int:pk>/', FruitDetails.as_view(), name='fruit_details'),
]