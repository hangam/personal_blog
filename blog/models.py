from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
	name = models.CharField(max_length=100)
	date_created = models.DateField(auto_now_add=True)
	slug = models.SlugField()

	def __str__(self):
		return self.name
	# def get_absolute_url(self):


class Blog(models.Model):
	title = models.CharField(max_length=100, null=False)
	content = models.TextField(null=False)
	# image  = models.ImageField(null=False
	updated_date = models.DateTimeField(auto_now_add=True, null=True)
	category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
	slug = models.SlugField(unique=True)


class User(AbstractUser):
	firstname = models.CharField(max_length=100, blank=True)
	lastname = models.CharField(max_length=100, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)


class Contact(models.Model):
	fullname = models.CharField(max_length=100, blank=False)
	address = models.CharField(max_length=100, blank=False)
	email = models.EmailField(max_length=100, blank=False)
	message = models.TextField(max_length=500, blank=False)

