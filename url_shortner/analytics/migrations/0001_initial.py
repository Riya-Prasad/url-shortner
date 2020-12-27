# Generated by Django 3.1.4 on 2020-12-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shrinkyy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('shrink_url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shrinkyy.shrinkurl')),
            ],
        ),
    ]