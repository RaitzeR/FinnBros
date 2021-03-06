# Generated by Django 2.0.4 on 2018-04-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0004_auto_20180427_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirebaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='buyer',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='food',
            name='is_bought',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='community',
            name='users',
            field=models.ManyToManyField(blank=True, to='foodapp.FirebaseUser'),
        ),
    ]
