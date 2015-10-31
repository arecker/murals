# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacting', '0002_message_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='subject',
            field=models.CharField(default='Test', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='address',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
    ]
