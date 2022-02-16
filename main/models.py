from django.db import models
# from django.shortcuts import render
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=40, verbose_name="Name")
    description = models.CharField(max_length=250, verbose_name="Description")
    sent_at = models.DateTimeField(auto_now_add=True)