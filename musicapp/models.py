from django.db import models
from datetime import datetime

# Create your models here.


# Creating Three(3) models: Artiste, Song and Lyrics.
class Artiste(models.Model):
    # class attribute for artiste
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return (self.first_name)  #specifing string method



class Song(models.Model):
    # class attribute for song
    artiste = models.ForeignKey("Artiste", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField()
    artiste_Id = models.IntegerField()

    def __str__(self):
        return (self.title)  #specifing string method


class Lyric(models.Model):
    song = models.ForeignKey("Song", on_delete=models.CASCADE)
    content = models.TextField() #attribute for lyrics
    song_Id = models.IntegerField()


    def __str__(self):
        return(self.song)   #specifing string method