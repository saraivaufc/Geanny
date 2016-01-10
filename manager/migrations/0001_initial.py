# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import manager.models.access


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizerKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=manager.models.access.generate_key, max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Organizer Key',
                'verbose_name_plural': 'Organizes Key',
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='organizerkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Creator', to='manager.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organizerkey',
            name='user',
            field=models.ForeignKey(related_name='Organizer', blank=True, to='manager.Organizer', null=True),
            preserve_default=True,
        ),
    ]
