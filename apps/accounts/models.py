"""
This model contains database design for all users and song artists
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver


from .manager import UserManager
from music_streamer.utils import unique_slug_generator

###################### user model
class User(AbstractBaseUser, PermissionsMixin):
    artist_name = models.CharField(
        max_length=255, 
        default='artist name', 
        unique=True
        )
    slug = models.SlugField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=300, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    # username = None


    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        # ordering = ('email',)
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        return str(self.email)

    def get_artist_name(self):
        return self.artist_name

    def get_short_name(self):
        return self.artist_name

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




def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(rl_pre_save_receiver, sender=User)



class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
         related_name="profile", 
         default=1
         )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    gender = models.CharField(max_length = 20, blank=True, null=True)
    record_label = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField()


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()