# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-31 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailapp', '0008_blogpage_advertisement')
    ]

    operations = [
        migrations.RenameModel(
            old_name='Advert',
            new_name='AdvertSnippet',
        )
    ]
