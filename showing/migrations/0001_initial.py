# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True)),
                ('title', models.CharField(max_length=150, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/')),
                ('in_carousel', models.BooleanField(default=True, verbose_name=b'In home carousel')),
                ('gallery', models.ForeignKey(blank=True, to='showing.Gallery', null=True)),
            ],
        ),
    ]
