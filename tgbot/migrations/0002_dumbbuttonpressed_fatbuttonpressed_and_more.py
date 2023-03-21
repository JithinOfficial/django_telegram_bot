# Generated by Django 4.1.7 on 2023-03-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DumbButtonPressed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dumb_btn_counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FatButtonPressed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fat_btn_counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StupidButtonPressed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stupid_btn_counter', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='tgusers',
            name='dumb_btn_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tgusers',
            name='fat_btn_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tgusers',
            name='stupid_btn_counter',
            field=models.IntegerField(default=0),
        ),
    ]
