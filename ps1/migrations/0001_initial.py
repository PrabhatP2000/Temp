# Generated by Django 3.2.5 on 2021-10-31 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('llMobile', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('passcode', models.IntegerField(default=1111)),
                ('careof', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('dist', models.CharField(blank=True, max_length=50)),
                ('house', models.CharField(blank=True, max_length=50)),
                ('landmark', models.CharField(blank=True, max_length=50)),
                ('loc', models.CharField(blank=True, max_length=50)),
                ('pc', models.CharField(blank=True, max_length=50)),
                ('po', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('subdist', models.CharField(blank=True, max_length=50)),
                ('vtc', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('resident_aadhaar', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('consent_status', models.BooleanField(null=True)),
                ('resMobile', models.CharField(default=9999999999, max_length=200)),
                ('careof', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('dist', models.CharField(blank=True, max_length=50)),
                ('house', models.CharField(blank=True, max_length=50)),
                ('landmark', models.CharField(blank=True, max_length=50)),
                ('loc', models.CharField(blank=True, max_length=50)),
                ('pc', models.CharField(blank=True, max_length=50)),
                ('po', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('subdist', models.CharField(blank=True, max_length=50)),
                ('vtc', models.CharField(blank=True, max_length=50)),
                ('llMobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ps1.landlord')),
            ],
        ),
    ]
