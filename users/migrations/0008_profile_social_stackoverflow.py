# Generated by Django 4.1 on 2022-11-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_skills_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_Stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
