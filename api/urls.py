from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from .views import *

router = routers.DefaultRouter()

router.register("employee", EmployeeViewset)
router.register("client", ClientViewset)
router.register("chambre", ChambreViewset)
router.register("reservation", ReservationViewset)
router.register("paiement", PaiementViewset)
router.register("commande", CommandeViewset)

urlpatterns = [
    path('', include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
