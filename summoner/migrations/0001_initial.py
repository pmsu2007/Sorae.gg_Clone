# Generated by Django 3.2.8 on 2022-01-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('champ_level', models.IntegerField()),
                ('champ_name', models.CharField(max_length=20)),
                ('kill', models.IntegerField()),
                ('death', models.IntegerField()),
                ('assist', models.IntegerField()),
                ('CS', models.IntegerField()),
                ('game_result', models.BooleanField()),
                ('play_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Summoner',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('summoner_level', models.IntegerField()),
                ('summoner_icon', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('solo_tier', models.CharField(max_length=20)),
                ('solo_rank', models.CharField(max_length=20)),
                ('solo_wins', models.IntegerField()),
                ('solo_losses', models.IntegerField()),
                ('solo_leaguePoints', models.IntegerField()),
                ('free_tier', models.CharField(max_length=20)),
                ('free_rank', models.CharField(max_length=20)),
                ('free_wins', models.IntegerField()),
                ('free_losses', models.IntegerField()),
                ('free_leaguePoints', models.IntegerField()),
            ],
        ),
    ]
