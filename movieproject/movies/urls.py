from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreViewSet, CustomerViewSet, TheaterViewSet, MovieViewSet,
    ScreeningViewSet, TicketViewSet, ReviewViewSet, UserViewSet, RoleViewSet
)

router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'theaters', TheaterViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'screenings', ScreeningViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
