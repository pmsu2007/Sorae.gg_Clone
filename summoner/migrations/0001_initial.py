# Generated by Django 3.2.8 on 2022-02-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailRecord',
            fields=[
                ('game_ID', models.CharField(max_length=33, primary_key=True, serialize=False)),
                ('match_ID', models.CharField(max_length=13)),
                ('summoner_name', models.CharField(max_length=20)),
                ('team_ID', models.SmallIntegerField()),
                ('minion_kill', models.SmallIntegerField()),
                ('jungle_kill', models.IntegerField()),
                ('champ_name', models.CharField(max_length=20)),
                ('champ_ID', models.SmallIntegerField()),
                ('champ_level', models.SmallIntegerField()),
                ('total_damage', models.IntegerField()),
                ('vision_score', models.SmallIntegerField()),
                ('primary_rune', models.SmallIntegerField()),
                ('sub_rune', models.SmallIntegerField()),
                ('item0', models.SmallIntegerField()),
                ('item1', models.SmallIntegerField()),
                ('item2', models.SmallIntegerField()),
                ('item3', models.SmallIntegerField()),
                ('item4', models.SmallIntegerField()),
                ('item5', models.SmallIntegerField()),
                ('item6', models.SmallIntegerField()),
                ('spell1', models.IntegerField()),
                ('spell2', models.IntegerField()),
            ],
            options={
                'ordering': ['-game_ID'],
            },
        ),
        migrations.CreateModel(
            name='GameRecord',
            fields=[
                ('game_ID', models.CharField(max_length=33, primary_key=True, serialize=False)),
                ('match_ID', models.CharField(max_length=13)),
                ('queue_ID', models.SmallIntegerField()),
                ('summoner_name', models.CharField(max_length=20)),
                ('champ_name', models.CharField(max_length=20)),
                ('champ_ID', models.SmallIntegerField()),
                ('kill', models.SmallIntegerField()),
                ('death', models.SmallIntegerField()),
                ('assist', models.SmallIntegerField()),
                ('game_result', models.BooleanField()),
                ('game_duration', models.IntegerField()),
                ('game_starttime', models.IntegerField()),
            ],
            options={
                'ordering': ['-game_ID'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('summoner_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('summoner_level', models.SmallIntegerField()),
                ('summoner_icon', models.SmallIntegerField()),
                ('solo_tier', models.CharField(max_length=20)),
                ('solo_rank', models.CharField(max_length=20)),
                ('solo_wins', models.SmallIntegerField()),
                ('solo_losses', models.SmallIntegerField()),
                ('solo_leaguePoints', models.SmallIntegerField()),
                ('solo_progress', models.CharField(max_length=5)),
                ('free_tier', models.CharField(max_length=20)),
                ('free_rank', models.CharField(max_length=20)),
                ('free_wins', models.SmallIntegerField()),
                ('free_losses', models.SmallIntegerField()),
                ('free_leaguePoints', models.SmallIntegerField()),
                ('free_progress', models.CharField(max_length=5)),
            ],
        ),
    ]
