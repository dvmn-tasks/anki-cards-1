# Generated by Django 2.2.16 on 2020-09-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anki_cards', '0025_basecard_enhancement'),
    ]

    operations = [
        migrations.AddField(
            model_name='basecard',
            name='status_card',
            field=models.CharField(choices=[('Ожидает проверки', 'wait'), ('Нужны доработки', 'improvements'), ('Одобрена', 'approved')], default='Ожидает проверки', max_length=40, verbose_name='Статус карточки'),
        ),
    ]
