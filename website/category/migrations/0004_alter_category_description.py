# Generated by Django 5.0.2 on 2024-03-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_rename_unique_code_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=600),
        ),
    ]