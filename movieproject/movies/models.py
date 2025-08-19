from django.db import models
from django.contrib.auth.models import AbstractUser
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)  # Django auto increments
    genre_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.genre_name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name or ''}".strip()


class Theater(models.Model):
    theater_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    total_seats = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name or f"Theater {self.theater_id}"


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name="movies")
    duration = models.PositiveIntegerField(blank=True, null=True)  # in minutes
    rating = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title


class Screening(models.Model):
    screening_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="screenings")
    show_time = models.DateTimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} @ {self.show_time}"


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE, related_name="tickets")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="tickets")
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.seat_number}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviews")
    rate = models.DecimalField(max_digits=3, decimal_places=1)  # 2,1 in Oracle
    comments = models.TextField(max_length=500, blank=True, null=True)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.movie} ({self.rate})"


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.role_name

class User(AbstractUser):
    hire_date = models.DateField(blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username



# Create your models here.
