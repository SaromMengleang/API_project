from rest_framework import viewsets
from .models import Genre, Customer, Theater, Movie, Screening, Ticket, Review, User, Role
from .serializers import (
    GenreSerializer, CustomerSerializer, TheaterSerializer, MovieSerializer,
    ScreeningSerializer, TicketSerializer, ReviewSerializer, UserSerializer, RoleSerializer
)
from rest_framework.permissions import IsAuthenticated
from .permissions import RolePermission
from rest_framework.pagination import PageNumberPagination


class MoviePageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated, RolePermission]
    pagination_class = MoviePageNumberPagination

# Create your views here.
