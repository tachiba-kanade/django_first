from unicodedata import category

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100) #uniquw
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"

class Game(models.Model):
    name = models.CharField(max_length=100) #unique
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"{self.id}"

class Score(models.Model):
    player = models.CharField.name = models.ForeignKey('Player', on_delete=models.CASCADE)(max_length=100) #ForeignKey?? or 
    game = models.CharField.name = models.ForeignKey('Game', on_delete=models.CASCADE)(max_length=100) #ForeignKey
    score = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"{self.id}"
