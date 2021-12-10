from django.db import models


# Create your models here.
class Categories(models.Model):
    categoryid = models.IntegerField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='categoryName', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    categorydescription = models.CharField(db_column='categoryDescription', max_length=100, blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categories'


class Counties(models.Model):
    countyname = models.CharField(db_column='countyName', primary_key=True, max_length=30) # Field name made lowercase.
    population = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'counties'
        unique_together = (('countyname', 'city'),)


class Covid(models.Model):
    patientid = models.CharField(db_column='patientID', primary_key=True, max_length=30) # Field name made lowercase.
    city = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'covid'


class Professors(models.Model):
    facultyid = models.CharField(db_column='facultyID', primary_key=True, max_length=30) # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    county = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professors'


class Students(models.Model):
    studentid = models.CharField(db_column='studentID', primary_key=True, max_length=30) # Field name made lowercase.
    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'