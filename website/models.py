from django.db import models 

class history(models.Model):
    
    class Meta:
        app_label = 'website'

    message = models.TextField(max_length=1000)
    anonymous = models.BooleanField(default=False)
    PFI = models.BooleanField(default=False)