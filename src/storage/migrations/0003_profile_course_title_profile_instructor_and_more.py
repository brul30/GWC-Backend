# Generated by Django 4.2.11 on 2024-04-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_profile_notes_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='course_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instructor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
