from django.db import models

# Create your models here.

class SourceConnectionDtls(models.Model):
    SrcId = models.AutoField(primary_key=True)
    SrcType = models.CharField(max_length=50)
    SrcNm = models.CharField(max_length=100)
    BigQueryProjectId = models.CharField(max_length=100)
    BigQueryServiceAccountKeyFileLocation = models.CharField(max_length=500)

class DestinationConnectionDtls(models.Model):
    DestId = models.AutoField(primary_key=True)
    DestType = models.CharField(max_length=50)
    DestNm = models.CharField(max_length=100) 
    DestUname = models.CharField(max_length=100)
    DestPwd = models.CharField(max_length=200)