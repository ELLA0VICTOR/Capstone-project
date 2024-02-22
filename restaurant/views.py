from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializers import Userserializer, Menuserializer, Bookingserializer
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import Menu_table, Booking_table


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [IsAuthenticated]
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = Menuserializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu_table.objects.all()
    serializer_class = Menuserializer
class BookingViewSet(ModelViewSet):
    queryset = Booking_table.objects.all()
    serializer_class= Bookingserializer