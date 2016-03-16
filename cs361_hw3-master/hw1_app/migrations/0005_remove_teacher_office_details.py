# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw1_app', '0004_auto_20151226_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='office_details',
        ),
    ]
