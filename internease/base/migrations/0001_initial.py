# Generated by Django 5.0.3 on 2024-04-02 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('support_leter', models.FileField(upload_to='support_leter')),
                ('photo', models.FileField(upload_to='photo')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Applications',
                'ordering': ('-created',),
            },
        ),
    ]
