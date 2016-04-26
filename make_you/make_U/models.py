from django.db import models
from django.conf import settings

class Contents(models.Model):
    user =  models.ForeignKey(settings.AUTH_USER_MODEL)
    summary = models.CharField(max_length=200)
    work_exp = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template = models.ForeignKey('Templates', blank=True, null=True )

class Templates(models.Model):
    template_image = models.ImageField(blank=True, null=True)
    order = models.SmallIntegerField(default=1, primary_key =True)
