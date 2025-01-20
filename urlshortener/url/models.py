from django.db import models
from django.utils.timezone import now, timedelta

def default_expiry():
    return now() + timedelta(hours=24)

class Url(models.Model):
    url_id = models.AutoField(primary_key=True)
    long_url = models.URLField(max_length=10000)
    short_url = models.CharField(max_length=10, unique=True)  
    created_at = models.DateTimeField(default=now) 
    expires_at = models.DateTimeField(default=default_expiry) 
    access_count = models.IntegerField(default=0) 
    password = models.CharField(max_length=100, blank=True, null=True) 
    def __str__(self):
        return self.long_url


class AccessLog(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE, related_name='logs') 
    timestamp = models.DateTimeField(default=now)  
    ip_address = models.GenericIPAddressField() 