# Generated by Django 2.0.1 on 2019-04-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER_LOGIN',
            fields=[
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('user_name', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=35)),
                ('pass_word', models.CharField(max_length=35)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
