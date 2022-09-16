from datetime import datetime
from distutils.command.upload import upload
from django.db import models

import datetime
import os
# Create your models here.

def filepath(request,filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow,old_filename)
    return os.path.join('uploads/',filename)

class user(models.Model):
    id = models.AutoField(primary_key=True)  
    file=models.ImageField(upload_to=filepath, null=True,blank=True)
    username = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    contact_number = models.CharField(max_length=100, null=True)
    vaccination_brand = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    vaccination_site = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    bday = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    directory = models.CharField(max_length=100, null=True)
    file_name = models.CharField(max_length=100, null=True)
    full_path = models.CharField(max_length=100, null=True)
    date_created  = models.DateField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table="user"

class sideeffect (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    muscle_ache = models.CharField(max_length=100, null=True)
    headache = models.CharField(max_length=100, null=True)
    fever = models.CharField(max_length=100, null=True)
    redness = models.CharField(max_length=100, null=True)
    swelling = models.CharField(max_length=100, null=True)
    tenderness = models.CharField(max_length=100, null=True)
    warmth = models.CharField(max_length=100, null=True)
    itch = models.CharField(max_length=100, null=True)
    induration = models.CharField(max_length=100, null=True)
    feverish = models.CharField(max_length=100, null=True)
    chills = models.CharField(max_length=100, null=True)
    join_pain = models.CharField(max_length=100, null=True)
    fatigue = models.CharField(max_length=100, null=True)
    nausea = models.CharField(max_length=100, null=True)
    vomiting = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table="sideeffect"

