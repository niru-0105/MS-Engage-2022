# Generated by Django 4.0.4 on 2022-05-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('image', models.ImageField(default='', upload_to='app1/images')),
                ('age', models.CharField(default='Not known', max_length=50)),
                ('plaeOfBirth', models.CharField(default='Not known', max_length=1000)),
                ('nationality', models.CharField(default='Not known', max_length=100)),
                ('gender', models.CharField(default='Not known', max_length=20)),
                ('weight', models.CharField(default='Not known', max_length=50)),
                ('height', models.CharField(default='Not known', max_length=50)),
                ('isWanted', models.BooleanField(default=False)),
                ('wantedInCountry', models.CharField(default='', max_length=100)),
                ('charges', models.CharField(default='', max_length=1000)),
                ('about', models.CharField(default='', max_length=10000)),
            ],
        ),
    ]