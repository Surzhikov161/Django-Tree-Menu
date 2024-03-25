# Generated by Django 5.0.3 on 2024-03-25 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menu_named_url_menuitem_named_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='data',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='link',
            field=models.URLField(blank=True, max_length=255),
        ),
    ]
