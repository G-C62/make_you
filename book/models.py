from django.db import models
from django.conf import settings

class Region(models.Model):
    name = models.CharField(max_length=200)

class Hashtag(models.Model):
    name = models.CharField(max_length=200)

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    restaurant = models.ForeignKey('Restaurant')


class Taste_user(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other_Gender'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    restaurant = models.ManyToManyField('Restaurant')   #Bookmark
    gender = models.CharField(
        max_length =1,
        choices = GENDER_CHOICES,
        default = None,
    )
    region_1 = models.ForeignKey('Region' , related_name = 'region_1')
    region_2 = models.ForeignKey('Region' , related_name = 'region_2')

class Restaurant(models.Model):

    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    main_menu = models.CharField(max_length=200)
    naver_geo_id = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    max_group_capacity = models.IntegerField()
    seats = models.IntegerField()
    hashtag = models.ManyToManyField('Hashtag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    num_of_people = models.SmallIntegerField()
    cost = models.PositiveIntegerField()
    rate = models.FloatField()

class Satisfaction(models.Model):
    meeting_rate = models.SmallIntegerField()
    meeting_comment = models.TextField()
    restaurant_rate = models.SmallIntegerField()
    restaurant_comment = models.TextField()
    user = models.ForeignKey('Taste_user')
    restaurant = models.ForeignKey('Restaurant')
    group = models.ForeignKey('Group')


class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey('Taste_user')
    record = models.ForeignKey('Record')


class Image(models.Model):
    image = models.ImageField()
    user =  models.ForeignKey('Taste_user')
    restaurant = models.ForeignKey('Restaurant')
    group = models.ForeignKey('Group')
