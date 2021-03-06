# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-18 10:23
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignRecognizeHistory',
            fields=[
                ('result_text', models.CharField(default=b'', max_length=256)),
                ('middle_symbol', models.CharField(default=b'', max_length=1024)),
                ('capture_armband', models.CharField(default=b'', max_length=64)),
                ('sign_request_id', models.IntegerField()),
                ('capture_id', models.AutoField(primary_key=True, serialize=False)),
                ('capture_date', models.DateTimeField(auto_now=True)),
                ('correctness', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SingleSignCapture',
            fields=[
                ('sign_text', models.CharField(default=b'', max_length=32)),
                ('capture_id', models.AutoField(primary_key=True, serialize=False)),
                ('sign_sentence_belong_id', models.IntegerField(default=-1)),
                ('correctness', models.BooleanField(default=False)),
                ('middle_symbol', models.CharField(default=b'', max_length=32)),
                ('raw_capture_data_acc', models.BinaryField(default=b'')),
                ('raw_capture_data_emg', models.BinaryField(default=b'')),
                ('raw_capture_data_gyr', models.BinaryField(default=b'')),
            ],
        ),
    ]
