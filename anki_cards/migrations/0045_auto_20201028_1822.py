# Generated by Django 2.2.11 on 2020-10-28 15:22
import uuid

from django.db import migrations, models


def fill_cards_guid(apps, schema_editor):
    BaseCard = apps.get_model('anki_cards', 'BaseCard')

    for card in BaseCard.objects.filter(models.Q(guid='') | models.Q(guid=None)):
        new_guid = str(uuid.uuid1())[:24]
        card.guid = new_guid  # uuid length is limited by Django data model
        card.save()


class Migration(migrations.Migration):

    dependencies = [
        ('anki_cards', '0044_auto_20201027_2241'),
    ]

    operations = [
        migrations.RunPython(fill_cards_guid),
    ]
