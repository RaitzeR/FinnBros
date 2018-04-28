# Generated by Django 2.0.4 on 2018-04-27 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='foodpost',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='foodpost',
            name='categories',
            field=models.ManyToManyField(blank=True, to='foodapp.Category'),
        ),
    ]