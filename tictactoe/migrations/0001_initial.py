# Generated by Django 4.0.5 on 2022-06-27 14:04

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('started_on', models.DateTimeField(default=datetime.datetime.now)),
                ('ended_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('move_x', models.SmallIntegerField(default=-1)),
                ('move_y', models.SmallIntegerField(default=-1, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(2)])),
                ('moved_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='ttt_game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(default=0, primary_key='id', serialize=False, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('registered_on', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddIndex(
            model_name='users',
            index=models.Index(fields=['username'], name='tictactoe_u_usernam_c03f0a_idx'),
        ),
        migrations.AddField(
            model_name='ttt_game',
            name='game_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='tictactoe.games'),
        ),
        migrations.AddField(
            model_name='moves',
            name='game_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='tictactoe.games'),
        ),
        migrations.AddField(
            model_name='moves',
            name='user_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='tictactoe.users'),
        ),
        migrations.AddField(
            model_name='games',
            name='winner_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tictactoe.users'),
        ),
        migrations.AddIndex(
            model_name='moves',
            index=models.Index(fields=['game_id'], name='tictactoe_m_game_id_edc1f8_idx'),
        ),
        migrations.AddIndex(
            model_name='moves',
            index=models.Index(fields=['user_id'], name='tictactoe_m_user_id_9c1550_idx'),
        ),
        migrations.AddIndex(
            model_name='games',
            index=models.Index(fields=['winner_user_id'], name='tictactoe_g_winner__8a53cb_idx'),
        ),
    ]
