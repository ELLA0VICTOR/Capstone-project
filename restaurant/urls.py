from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *




router = DefaultRouter()

router.register(r'users', UserViewSet)


urlpatterns=[
   
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]