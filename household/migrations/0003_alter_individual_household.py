# Generated by Django 3.2.15 on 2022-08-25 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='household',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='individuals', to='household.household'),
        ),
    ]
