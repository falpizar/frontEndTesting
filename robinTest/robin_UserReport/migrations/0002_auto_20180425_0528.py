# Generated by Django 2.0.4 on 2018-04-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robin_UserReport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePagePresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_id', models.CharField(help_text='Some introductory data for the new users. This points to data accessible to all users.', max_length=15)),
            ],
        ),
        migrations.RenameModel(
            old_name='Application_User',
            new_name='ApplicationUser',
        ),
    ]
