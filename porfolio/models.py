from django.db import models

# Create your models here.
class Usages(models.Model):
  id = models.AutoField(primary_key=True)
  techTitle = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
class Jobs(models.Model):
  id = models.AutoField(primary_key=True)
  logo = models.CharField(max_length=100)
  company = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  start_date = models.DateField()
  end_date = models.DateField()
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
class Projects(models.Model):
  id = models.AutoField(primary_key=True)
  uid = models.CharField(max_length=100)
  src = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  desc = models.TextField()
  url = models.URLField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
class Tools(models.Model):
  id = models.AutoField(primary_key=True)
  usage_id = models.ForeignKey(Usages, on_delete = models.CASCADE, related_name="tools")
  url = models.CharField(max_length=100)
  tool = models.CharField(max_length=100)
  desc = models.TextField()
  href = models.URLField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  