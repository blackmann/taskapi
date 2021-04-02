from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
  name = models.CharField(max_length=50)
  address = models.TextField()

  def __str__(self) -> str:
      return self.name

class Department(models.Model):
  company = models.ForeignKey(Company, related_name="departments", on_delete=models.CASCADE)
  title = models.CharField(max_length=50)

  def __str__(self) -> str:
      return self.company.name + ' - ' + self.title

class Employee(models.Model):
  user = models.ForeignKey(User, related_name="employee_profile", on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  department = models.ForeignKey(Department, related_name="employees", on_delete=models.CASCADE)
  position = models.CharField(max_length=20) # eg. Programmer, Secretary, etc
  avatar = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
      return self.user.username


class Task(models.Model):
  completed = models.BooleanField(default=False)
  title = models.CharField(max_length=60)
  description = models.CharField(max_length=240)
  deadline = models.DateTimeField()
  employee = models.ForeignKey(Employee, related_name="tasks", on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)


# create your models (after planning them carefully)