# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacting', '0003_auto_20151031_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
