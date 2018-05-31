# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-31 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailapp', '0010_auto_20180531_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogAdvertPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('blog_index_page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='advert_placements', to='wagtailapp.BlogIndexPage')),
                ('its_advert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailapp.AdvertSnippet')),
            ],
            options={
                'verbose_name': 'advert placement',
                'verbose_name_plural': 'advert placements',
            },
        ),
    ]
