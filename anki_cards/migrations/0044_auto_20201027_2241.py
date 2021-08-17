# Generated by Django 2.2.11 on 2020-10-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anki_cards', '0043_englishcard_acting_voice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecard',
            name='guid',
            field=models.CharField(help_text='Globally unique id, almost certainly used for syncing', max_length=24, null=True, unique=True),
        ),
    ]
