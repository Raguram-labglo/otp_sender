from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_mobile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE, related_name='mobile_no')
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    recived_otp = models.IntegerField(null=True)

    def __str__(self):
        return str(self.Mobile)
