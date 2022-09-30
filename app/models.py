from django.db import models

# Create your models here.
class Meteric(models.Model):
    metering_code = models.CharField(max_length=30)
    timestamp_utc = models.CharField(max_length=30)