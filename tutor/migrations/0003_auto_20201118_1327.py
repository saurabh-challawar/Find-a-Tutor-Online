# Generated by Django 3.1.2 on 2020-11-18 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_auto_20201118_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.userinfo'),
        ),
    ]
