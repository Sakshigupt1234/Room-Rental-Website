# Generated by Django 4.0 on 2022-01-19 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_room_alter_feedback_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=20, null=True)),
                ('full_name', models.CharField(max_length=20, null=True)),
                ('email_id', models.CharField(max_length=20, null=True)),
                ('mobile1', models.CharField(max_length=20, null=True)),
                ('mobile2', models.CharField(max_length=20, null=True)),
                ('booking_date', models.CharField(max_length=20, null=True)),
                ('days', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=20, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
