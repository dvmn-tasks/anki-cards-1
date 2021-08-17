# Generated by Django 2.2.17 on 2021-01-14 12:36

import anki_cards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anki_cards', '0056_auto_20201118_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecard',
            name='guid',
            field=models.CharField(db_index=True, default=anki_cards.models.generate_card_guid, help_text='Globally unique id, almost certainly used for syncing', max_length=36, unique=True),
        ),
    ]
