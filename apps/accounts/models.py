"""
This model contains database design for all users and song artists
"""


from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import *


###################### user model
class User(AbstractBaseUser):
    artist_name = models.CharField(max_length=255, default='artist_name')
    email = models.CharField(max_length = 300, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['artist_name']

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
         related_name="userprofile", default=1
         )
    first_name = models.CharField(max_length=255, blank = True, null = True)
    last_name = models.CharField(max_length=255, blank = True, null = True)
    country = models.CharField(max_length=500, blank = True, null = True)
    gender = models.CharField(max_length = 20, blank = True, null = True)
    record_label = models.CharField(max_length=255, blank = True, null = True)
    image  = models.FileField( upload_to="artist/")


