# Generated by Django 4.1.5 on 2023-01-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('V', 'A venda'), ('C', 'Comprado')], default='V', max_length=1),
        ),
    ]
