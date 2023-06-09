# Generated by Django 4.2 on 2023-04-08 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0002_remove_category_title_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Мои задачи'),
        ),
        migrations.AlterField(
            model_name='currenttasks',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='get_task', to='affairs.category', verbose_name='Мои задачи'),
        ),
    ]
