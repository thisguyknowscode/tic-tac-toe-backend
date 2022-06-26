from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ttt_users(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['username', ],)
        ]
    id = models.IntegerField(primary_key='id', default=0, unique=True)
    username = models.CharField(unique=True, max_length=255)
    registeredOn = models.DateTimeField(default=datetime.now)


class ttt_game(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['winnerUserId', ]),
        ]
    id = models.IntegerField(primary_key=True, unique=True)
    winnerUserId = models.ForeignKey(
        to=ttt_users, to_field='id', on_delete=models.CASCADE)
    startedOn = models.DateTimeField(default=datetime.now)
    endedOn = models.DateTimeField(default=datetime.now)


class ttt_move(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['gameId', ]),
            models.Index(fields=['userId', ]),
        ]
    id = models.IntegerField(primary_key=True, unique=True)
    gameId = models.ForeignKey(
        ttt_game, on_delete=models.CASCADE, default=-1)
    userId = models.ForeignKey(
        ttt_users, on_delete=models.CASCADE, default=-1)
    moveX = models.SmallIntegerField(default=-1)
    moveY = models.SmallIntegerField(
        default=-1, validators=[MinValueValidator(-1), MaxValueValidator(2)])
    movedOn = models.DateTimeField(default=datetime.now)
