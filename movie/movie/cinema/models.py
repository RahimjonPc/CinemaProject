from django.db import models



class Movie(models.Model):
    name = models.CharField('name', max_length=50)
    description = models.TextField('description')

    

    def __str__(self):
        return self.name


class MoviePlay(models.Model):
    movie = models.CharField('movie', max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    available_seats = models.IntegerField()


    def __str__(self):
        return self.movie


class Booking(models.Model):
    name_customer = models.CharField('name', max_length=50)
    name_movie = models.CharField('film', max_length=50)
    customer_seats = models.IntegerField()


    def __str__(self):
        return self.name_customer
