from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=100)
    artists = models.ManyToManyField('Artist')
    entertainment = models.ForeignKey('Entertainment', on_delete=models.CASCADE)
    released_date = models.DateField()

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=50)
    birth = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entertainment(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name