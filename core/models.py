from django.db import models

# Create your models here.


class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class RequestStore(ModelBase):
    path = models.CharField(max_length=255)
    time = models.FloatField()
    query_coount = models.IntegerField()