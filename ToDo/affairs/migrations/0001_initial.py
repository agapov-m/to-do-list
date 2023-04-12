# Generated by Django 4.2 on 2023-04-04 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Мои задачи')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='CurrentTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Текущие задачи')),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='affairs.category', verbose_name='Мои задачи')),
            ],
            options={
                'verbose_name': 'Текущая задача',
                'verbose_name_plural': 'Текущие задачи',
            },
        ),
        migrations.CreateModel(
            name='CompletedTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Выполненные')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='affairs.category', verbose_name='Мои задачи')),
            ],
            options={
                'verbose_name': 'Завершенная задача',
                'verbose_name_plural': 'Завершенные задачи',
            },
        ),
    ]