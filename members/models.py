from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    susf_expiry = models.DateField('SUSF Expiry Date')
    club_expiry = models.DateField('Club membership Expiry Date')
    dob = models.DateField('Date of Birth')
    comments = models.TextField()
    email = models.EmailField('Email Address')
    student = models.BooleanField('Is a Student')

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
