from django.urls import path
from .api.StadiumCreate.views import StadiumCreateAPIView
from .api.StadiumCount.views import StadiumCountAPIView
from .api.StadiumUpdateDestroy.views import StadiumUpdateDestroyAPIView
from .api.StadiumCreateOwner.views import StadiumCreateOwnerAPIView
from .api.StadiumListOwner.views import StadiumListOwnerAPIView
from .api.StadiumManagerCreate.views import StadiumManagerCreateAPIView
from .api.StadiumListForUser.views import StadiumListUserAPIView


urlpatterns = [
    path('stadium-create/', StadiumCreateAPIView.as_view(), name='stadium-create'),
    path('stadium-count/', StadiumCountAPIView.as_view(), name='stadium-count'),
    path('stadium-update-destroy/<int:pk>/', StadiumUpdateDestroyAPIView.as_view(), name='stadium-update-destroy'),
    path('stadium-create-owner/', StadiumCreateOwnerAPIView.as_view(), name='stadium-creat-owner'),
    path('stadium-list-owner/', StadiumListOwnerAPIView.as_view(), name='stadium-list-owner'),
    path('stadium-manager-create/', StadiumManagerCreateAPIView.as_view(), name='stadium-manager-create'),
    path('stadium-list-user/', StadiumListUserAPIView.as_view(), name='stadium-list-user'),
]
