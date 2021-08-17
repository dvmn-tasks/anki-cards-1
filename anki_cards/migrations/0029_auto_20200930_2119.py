# Generated by Django 2.2.16 on 2020-09-30 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anki_cards', '0028_auto_20200930_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basecard',
            name='card_status',
            field=models.CharField(blank=True, choices=[('wait', 'Ожидает проверки'), ('improvements', 'Нужны доработки'), ('approved', 'Одобрена')], default='wait', max_length=40, verbose_name='Статус карточки'),
        ),
        migrations.AlterField(
            model_name='basecard',
            name='deck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards', to='anki_cards.Deck', verbose_name='Колода'),
        ),
    ]
