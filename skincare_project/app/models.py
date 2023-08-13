from django.db import models
import argparse

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)