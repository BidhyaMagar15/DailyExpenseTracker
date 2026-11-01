from django.db import models



class UserProfile(models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.name or "Unnamed User"