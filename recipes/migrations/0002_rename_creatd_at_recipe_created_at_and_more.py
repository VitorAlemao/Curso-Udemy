# Generated by Django 4.1.1 on 2022-10-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='creatd_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(
                blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]
