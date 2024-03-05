from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

DEPARTMAN_CHOICES = [ 
        ('Fullstack', 'Fullstack'),
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend')
    ]

class Departman(models.Model):
    name = models.CharField(max_length=100, choices=DEPARTMAN_CHOICES)
   
    def __str__(self):
        return self.name
    
    def total_people(self):
        return self.personel.count() 

   

class Personel(models.Model):
    

    TITLE_CHOICES = [
        ('TL', 'Team Lead'),
        ('ML', 'Mid Lead'),
        ('J', 'Junior'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    departman = models.ForeignKey(Departman, on_delete=models.CASCADE, related_name= "personel")
    user = models.ForeignKey(User, on_delete=models.PROTECT )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def calculate_working_days(self):
        today = date.today()
        working_days = (today - self.start_date).days
        return working_days
    
   
