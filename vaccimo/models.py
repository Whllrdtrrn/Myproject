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
    name = models.CharField(max_length=100, default='None')
    muscle_ache = models.CharField(max_length=100, default='None')
    headache = models.CharField(max_length=100, default='None')
    fever = models.CharField(max_length=100, default='None')
    redness = models.CharField(max_length=100, default='None')
    swelling = models.CharField(max_length=100, default='None')
    tenderness = models.CharField(max_length=100, default='None')
    warmth = models.CharField(max_length=100, default='None')
    itch = models.CharField(max_length=100, default='None')
    induration = models.CharField(max_length=100, default='None')
    feverish = models.CharField(max_length=100, default='None')
    chills = models.CharField(max_length=100, default='None')
    join_pain = models.CharField(max_length=100, default='None')
    fatigue = models.CharField(max_length=100, default='None')
    nausea = models.CharField(max_length=100, default='None')
    vomiting = models.CharField(max_length=100, default='None')
    def __str__(self):
        return self.name

    class Meta:
        db_table="sideeffect"


class questioner (models.Model): 

    id = models.AutoField(primary_key=True)
    Q0 = models.CharField(max_length=100, null=True)
    Q1 = models.CharField(max_length=100, null=True)
    Q2 = models.CharField(max_length=100, null=True)
    Q3 = models.CharField(max_length=100, null=True)
    Q4 = models.CharField(max_length=100, null=True)
    Q5 = models.CharField(max_length=100, null=True)
    Q6 = models.CharField(max_length=100, null=True)
    Q7 = models.CharField(max_length=100, null=True)
    Q8 = models.CharField(max_length=100, null=True)
    Q9 = models.CharField(max_length=100, null=True)
    Q10 = models.CharField(max_length=100, null=True)
    Q11 = models.CharField(max_length=100, null=True)
    Q12 = models.CharField(max_length=100, null=True)
    Q13 = models.CharField(max_length=100, null=True)
    Q14 = models.CharField(max_length=100, null=True)
    Q15 = models.CharField(max_length=100, null=True)
    Q16 = models.CharField(max_length=100, null=True)
    Q17 = models.CharField(max_length=100, null=True)
    Q18 = models.CharField(max_length=100, null=True)
    Q19 = models.CharField(max_length=100, null=True)
    Q20 = models.CharField(max_length=100, null=True)
    Q21 = models.CharField(max_length=100, null=True)
    Q22 = models.CharField(max_length=100, null=True)
    allergy = models.CharField(max_length=100, null=True)
    Q23 = models.CharField(max_length=100, null=True)
    Q24 = models.CharField(max_length=100, null=True)

   

    class Meta:
        db_table="questioner"