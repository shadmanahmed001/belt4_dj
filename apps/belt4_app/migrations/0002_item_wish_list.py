# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 03:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt4_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt4_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Wish_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('itemsadded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt4_app.Item')),
                ('useradding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='belt4_app.User')),
            ],
        ),
    ]