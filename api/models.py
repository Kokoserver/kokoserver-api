from django.db import models
from django.conf import settings
# Create your models here.
def uploadDirectory(instance, filename):
     return f"status/{instance.user}/{filename}"
class StatusQueryset(models.QuerySet):
     pass
 
class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQueryset(self.model, using=self._db)
 
class Status(models.Model):
    user   = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=uploadDirectory ,null=True, blank=True, default="No image")
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = StatusManager()
    
    def __str__(self):
        return str(self.content)[:50]
    
    class Meta:
        verbose_name = "status post"
        verbose_name_plural = "status posts"