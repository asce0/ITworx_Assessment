from django.urls import path
from .views import EntityGatharingApiView

urlpatterns = [
    path('analysis/', EntityGatharingApiView.as_view()),
]