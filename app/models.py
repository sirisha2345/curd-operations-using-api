from django.db import models

# Create your models here
class dept(models.Model):
    detno=models.IntegerField()
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return self.dname
class emp(models.Model):
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE) 
    ename=models.CharField(max_length=100)   
    eid=models.IntegerField()
    esal=models.IntegerField()
    ejob=models.CharField(max_length=100)
