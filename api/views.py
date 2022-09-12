from typing import List

from rest_framework import viewsets
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class EmployeeViewset(viewsets.ModelViewSet):
	serializer_class = EmployeeSerializer
	queryset = Employee.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class ClientViewset(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class ChambreViewset(viewsets.ModelViewSet):
	serializer_class = ChambreSerializer
	queryset = Chambre.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class ReservationViewset(viewsets.ModelViewSet):
	serializer_class = ReservationSerializer
	queryset = Reservation.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class PaiementViewset(viewsets.ModelViewSet):
	serializer_class = PaiementSerializer
	queryset = Paiement.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]

class CommandeViewset(viewsets.ModelViewSet):
	serializer_class = CommandeSerializer
	queryset = Commande.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [AllowAny]
