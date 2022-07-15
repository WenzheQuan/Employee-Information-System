from django.db import models

# Create your models here.

class Department(models.Model):
    """department table"""
    title = models.CharField(verbose_name="title", max_length=32)

    """Decide what content it shows"""
    def __str__(self):
        return self.title

class UserInfo(models.Model):

    name = models.CharField(verbose_name="Name",max_length=16)
    password = models.CharField(verbose_name="Password", max_length=64)
    age = models.IntegerField(verbose_name="Age")
    account = models.DecimalField(verbose_name="Account", max_digits=10, decimal_places=2, default=0)
    #start_time = models.DateTimeField(verbose_name="Start_time")
    start_time = models.DateField(verbose_name="Start_time")

    #foreign key, id is generated automatically
    depart = models.ForeignKey(verbose_name="Department",to="Department", to_field="id", on_delete=models.CASCADE)

    #set gender
    gender_choices = (
        (1,'Male'),
        (2,'Female'),
                      )
    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_choices)


class SuperNum(models.Model):
    mobile = models.CharField(verbose_name="Mobile", max_length=32)
    price = models.IntegerField(verbose_name="Price")
    level_choices =(
        (1,'Low'),
        (2,'Mid'),
        (3,'High')
    )
    level = models.SmallIntegerField(verbose_name="Level", choices=level_choices, default=1)

    status_choices = (
        (1,'Available'),
        (2,'Occupied')
    )
    status = models.SmallIntegerField(verbose_name="Status", choices=status_choices)

