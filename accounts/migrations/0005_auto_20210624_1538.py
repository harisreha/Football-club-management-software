# Generated by Django 3.2 on 2021-06-24 22:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210516_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('modul', models.CharField(max_length=200)),
                ('datumIzmjene', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('tipPromjene', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='members',
            name='napomena',
        ),
        migrations.AddField(
            model_name='players',
            name='plata',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staff',
            name='plata',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
