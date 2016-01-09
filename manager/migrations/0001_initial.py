# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_image', models.ImageField(default=None, upload_to=b'documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Phone', blank=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address', blank=True)),
                ('exists', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_joined'],
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='manager.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizes',
            },
            bases=('manager.person',),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='manager.Person')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Attendee',
                'verbose_name_plural': 'Attendees',
            },
            bases=('manager.person',),
        ),
    ]
