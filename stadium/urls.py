from django.urls import path

from .api.StadiumCreate.views import StadiumCreateAPIView
from .api.StadiumCount.views import StadiumCountAPIView
from .api.StadiumUpdateDestroy.views import StadiumUpdateDestroyAPIView


urlpatterns = [
    path('stadium-create/', StadiumCreateAPIView.as_view(), name='stadium-create'),
    path('stadium-count/', StadiumCountAPIView.as_view(), name='stadium-count'),
    path('stadium-update-destroy/<int:pk>/', StadiumUpdateDestroyAPIView.as_view(), name='stadium-update-destroy'),
]
