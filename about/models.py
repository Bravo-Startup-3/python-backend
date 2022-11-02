from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Pricing(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Services(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Terms(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

class Privacy(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()