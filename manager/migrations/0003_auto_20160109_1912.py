# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_attendeekey_organizerkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendeekey',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='attendeekey',
            name='user',
        ),
        migrations.DeleteModel(
            name='AttendeeKey',
        ),
    ]
