# Generated by Django 4.2.11 on 2024-04-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notes_pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]