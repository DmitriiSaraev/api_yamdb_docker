# Generated by Django 3.2 on 2022-12-20 03:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_merge_0003_auto_20221218_0400_0003_auto_20221218_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genresoftitle',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles_of_genre', to='reviews.genre'),
        ),
        migrations.AlterField(
            model_name='genresoftitle',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title_genres', to='reviews.title'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(db_index=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='UniqueReviewCOnstraint'),
        ),
    ]
