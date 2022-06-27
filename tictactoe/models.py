from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Users(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['username', ],)
        ]
    id = models.IntegerField(primary_key='id', default=0, unique=True)
    username = models.CharField(unique=True, max_length=255)
    registered_on = models.DateTimeField(default=datetime.now)


class Games(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['winner_user_id', ]),
        ]
    id = models.IntegerField(primary_key=True, unique=True)
    winner_user_id = models.ForeignKey(
        to=Users, to_field='id', on_delete=models.CASCADE)
    started_on = models.DateTimeField(default=datetime.now)
    ended_on = models.DateTimeField(default=datetime.now)


class Moves(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['game_id', ]),
            models.Index(fields=['user_id', ]),
        ]
    id = models.IntegerField(primary_key=True, unique=True)
    game_id = models.ForeignKey(
        Games, on_delete=models.CASCADE, default=-1)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE, default=-1)
    move_x = models.SmallIntegerField(default=-1)
    move_y = models.SmallIntegerField(
        default=-1, validators=[MinValueValidator(-1), MaxValueValidator(2)])
    moved_on = models.DateTimeField(default=datetime.now)


class ttt_game(models.Model):
    game_id = models.ForeignKey(
        Games, on_delete=models.CASCADE, default=-1)
