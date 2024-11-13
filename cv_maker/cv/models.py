# models.py
from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="Position not specified")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    # Other fields


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50)
    personal_info = models.ForeignKey(PersonalInfo, related_name='skills', on_delete=models.CASCADE)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, related_name='education', on_delete=models.CASCADE)

class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    responsibilities = models.TextField()
    personal_info = models.ForeignKey(PersonalInfo, related_name='work_experience', on_delete=models.CASCADE)
