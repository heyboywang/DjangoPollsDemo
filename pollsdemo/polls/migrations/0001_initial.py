# Generated by Django 2.2 on 2019-04-18 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=20)),
                ('votes', models.IntegerField(max_length=255)),
                ('oQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Questions')),
            ],
        ),
    ]
