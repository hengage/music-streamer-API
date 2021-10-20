"""
This model contains all the database design models for 'sonngs, 'albums' and 'playlists'.
"""

from django.db import models
from django.conf import settings
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


from music_streamer.utils import unique_slug_generator



def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Album(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
         related_name='album_artist'
    )
    audio_file = models.FileField()
    genre = models.CharField(max_length=255)
    year = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        blank=True
    )
    cover_image = models.FileField()

    
    def __str__(self):
        return f"{self.title} - {self.artist}"

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)



class Song(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, null=True, blank=True,unique=True)
    artist = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE, 
    related_name='song_artist'
    )
    audio_file = models.FileField()
    album = models.ForeignKey(
        Album,
        on_delete=models.PROTECT,
        blank=True,
        null=True)
    genre = models.CharField(max_length=255)
    year = models.IntegerField(
        default=current_year(),
        validators=[MinValueValidator(1984), max_value_current_year]
    )
    uploaded_at = models.DateTimeField(default=timezone.now)
    duration = models.DecimalField(
        max_digits=4, 
        decimal_places=2,
        blank=True
        )
    cover_image = models.FileField()

   
    def __str__(self):
        return f"{self.title} - {self.artist}"

    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

# def rl_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance.title)


# pre_save.connect(rl_pre_save_receiver, sender=Song)