# Generated by Django 3.2 on 2022-12-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(default='295413', max_length=255, null=True, verbose_name='Код подтверждения'),
        ),
    ]
