# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw1_app', '0005_remove_teacher_office_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='office_details',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
