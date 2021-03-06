# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_professormessage_users_that_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professormessage',
            name='users_that_read',
            field=models.ManyToManyField(related_name='read_messages', null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
