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
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('location', models.CharField(max_length=75, null=True, verbose_name='location', blank=True)),
                ('last_seen', models.DateTimeField(auto_now=True, verbose_name='last seen')),
                ('last_ip', models.GenericIPAddressField(null=True, verbose_name='last ip', blank=True)),
                ('is_administrator', models.BooleanField(default=False, verbose_name='administrator status')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='moderator status')),
                ('first_name', models.CharField(help_text='Please enter you first name.', max_length=100, null=True, verbose_name='First Name ')),
                ('last_name', models.CharField(help_text='Please enter you last name.', max_length=100, null=True, verbose_name='Last Name ')),
                ('username', models.CharField(help_text='Please enter you username.', unique=True, max_length=30, verbose_name='Username', db_index=True)),
                ('email', models.EmailField(help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to=b'documents/image/profile_image/%Y/%m/%d', blank=True, help_text='Please enter you profile image.', null=True, verbose_name='Profile Image')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='Phone', blank=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address', blank=True)),
                ('exists', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date_joined'],
                'abstract': False,
                'verbose_name_plural': 'Persons',
                'db_table': 'auth_user',
                'verbose_name': 'Person',
                'swappable': 'AUTH_USER_MODEL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Please enter the name of the activity.', max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='Please enter a description of the activity.', verbose_name='Description')),
                ('type', models.CharField(help_text='Please enter the type of your event.', max_length=255, verbose_name='Type', choices=[(b'LECTURE', 'Lecture'), (b'COURSE', 'Course')])),
                ('start_hour', models.TimeField(help_text='Please enter the starting hour of the activity.', verbose_name='Start Hour')),
                ('end_hour', models.TimeField(help_text='Please enter the end date of the activity.', verbose_name='End Hour')),
                ('value', models.FloatField(default=0.0, help_text='Please choose the registration fee.', verbose_name='Value')),
                ('image', models.ImageField(default=None, upload_to=b'documents/image/activity/%Y/%m/%d', blank=True, help_text='Please choose an image for the profile of your activity.', null=True, verbose_name='Imagem')),
                ('capacity', models.IntegerField(help_text='Please ability of people to your activity supports.', verbose_name='Capacity')),
                ('active', models.BooleanField(default=False, help_text='Please check this box if you want to publish your activity.', verbose_name='Active')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activitis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(help_text=b'Format: XXXXX-XXX', max_length=9, verbose_name='CEP')),
                ('street', models.CharField(help_text='Please enter street.', max_length=255, verbose_name='Street')),
                ('district', models.CharField(help_text='Please enter district.', max_length=255, verbose_name='District')),
                ('city', models.CharField(help_text='Please enter city.', max_length=255, verbose_name='City')),
                ('state', models.CharField(help_text='Please enter state.', max_length=255, verbose_name='State')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['cep'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Attendee',
                'verbose_name_plural': 'Attendees',
            },
            bases=('manager.person',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Please enter the name of the activity.', max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='Please enter a description of the activity.', verbose_name='Description')),
                ('type', models.CharField(help_text='Please enter the type of your event.', max_length=100, verbose_name='Type', choices=[(b'PRESENTIAL', 'Presential'), (b'ONLINE', 'Online')])),
                ('start_date', models.DateField(help_text='Please enter the starting date of the event.', verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='Please enter the end date of the event.', verbose_name='End Date')),
                ('capacity', models.IntegerField(help_text='Please ability of people to your event supports.', verbose_name='Capacity')),
                ('value', models.FloatField(default=0.0, help_text='Please choose the registration fee.', verbose_name='Value')),
                ('image', models.ImageField(default=None, upload_to=b'documents/image/event/%Y/%m/%d', blank=True, help_text='Please choose an image for the profile of your event.', null=True, verbose_name='Imagem')),
                ('active', models.BooleanField(default=False, help_text='Please check this box if you want to publish your event.', verbose_name='Active')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('address', models.ForeignKey(verbose_name='Address', blank=True, to='manager.Address', null=True)),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Please enter name.', max_length=255, verbose_name='Name')),
                ('decription', models.TextField(help_text='Please enter description.', verbose_name='Description')),
                ('image', models.ImageField(default=None, upload_to=b'documents/image/event/%Y/%m/%d', blank=True, help_text='Please choose an image for the profile of organization.', null=True, verbose_name='Imagem')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Organizer',
                'verbose_name_plural': 'Organizes',
            },
            bases=('manager.person',),
        ),
        migrations.CreateModel(
            name='OrganizerKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=manager.models.access.generate_key, max_length=100, verbose_name='Key')),
                ('in_use', models.BooleanField(default=False, verbose_name='In Use')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('creator', models.ForeignKey(verbose_name='Creator', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='Organizer', blank=True, to='manager.Organizer', null=True)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Organizer Key',
                'verbose_name_plural': 'Organizes Key',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField(default=0.0, verbose_name='Value')),
                ('is_maturity', models.BooleanField(default=False, verbose_name='Maturity')),
                ('maturity_date', models.DateTimeField(verbose_name='Maturity Date')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('paid_value', models.FloatField(default=0.0, verbose_name='Value')),
                ('paid_date', models.DateTimeField(null=True, verbose_name='Paid Date', blank=True)),
                ('monthly_interest', models.FloatField(default=0.0, verbose_name='Monthly Interest')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('user', models.ForeignKey(verbose_name='Person', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegistrationActivity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accredited', models.BooleanField(default=False, verbose_name='Accredited')),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration Date')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('activity', models.ForeignKey(verbose_name='Activity', to='manager.Activity')),
                ('attendee', models.ForeignKey(verbose_name='Attendee', to='manager.Attendee')),
                ('payments', models.ManyToManyField(default=None, to='manager.Payment', verbose_name='Payments')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegistrationEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('accredited', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('attendee', models.ForeignKey(verbose_name='Attendee', to='manager.Attendee')),
                ('event', models.ForeignKey(verbose_name='Event', to='manager.Event')),
                ('payments', models.ManyToManyField(default=None, to='manager.Payment', verbose_name='Payments')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addreses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Please enter the name of the resource.', max_length=255, verbose_name='Name')),
                ('description', models.TextField(help_text='Please enter a description of the resource.', verbose_name='Description')),
                ('type', models.CharField(help_text='Please enter the type of resource.', max_length=255, verbose_name='Type', choices=[(b'LECTURE', 'Lecture'), (b'COURSE', 'Course'), (b'INSTRUCTOR', 'Instructor'), (b'MATERIAL', 'Material'), (b'ROOM', 'Room')])),
                ('priority', models.CharField(help_text='Please enter the priority of resource.', max_length=255, verbose_name='Priority', choices=[(b'LOW', 'Low'), (b'NORMAL', 'Normal'), (b'HIGH', 'High')])),
                ('value', models.FloatField(default=1, help_text='Please choose the quantity of resource.', verbose_name='Value')),
                ('quantity', models.FloatField(default=1, help_text='Please choose the quantity of resource.', verbose_name='Quantity')),
                ('image', models.ImageField(default=None, upload_to=b'documents/image/resource/%Y/%m/%d', blank=True, help_text='Please choose an image for the profile of your activity.', null=True, verbose_name='Imagem')),
                ('active', models.BooleanField(default=False, help_text='Please check this box if you want to publish your resource.', verbose_name='Active')),
                ('creation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('exists', models.BooleanField(default=True, verbose_name='Exists')),
                ('activity', models.ForeignKey(verbose_name='Activity', to='manager.Activity')),
                ('event', models.ForeignKey(verbose_name='Event', to='manager.Event')),
            ],
            options={
                'ordering': ['creation'],
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activitis',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(verbose_name='Event', to='manager.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
