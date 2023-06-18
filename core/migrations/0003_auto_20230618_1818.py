# Generated by Django 3.2.12 on 2023-06-18 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230616_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=10)),
            ],
            options={
                'verbose_name': 'Tool',
                'verbose_name_plural': 'Tools',
            },
        ),
        migrations.AddField(
            model_name='recentwork',
            name='begindate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recentwork',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recentwork',
            name='enddate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='recentwork',
            name='tecnologies',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='personalprojects',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='personalprojects',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]