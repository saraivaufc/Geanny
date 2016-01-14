# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_remove_person_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='code',
        ),
        migrations.RemoveField(
            model_name='event',
            name='code',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='code',
        ),
        migrations.RemoveField(
            model_name='registrationactivity',
            name='code',
        ),
        migrations.RemoveField(
            model_name='registrationevent',
            name='code',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='code',
        ),
        migrations.AddField(
            model_name='activity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationactivity',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationevent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resource',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(help_text='Please enter the type of your event.', max_length=100, verbose_name='Type', choices=[(b'PRESENTIAL', 'Presential'), (b'ONLINE', 'Online')]),
            preserve_default=True,
        ),
    ]
