# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-09-13 22:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='notes',
        ),
    ]
