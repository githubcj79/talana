# Generated by Django 3.0.5 on 2020-04-28 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('doors', models.IntegerField()),
                ('diesel', models.BooleanField()),
                ('persons', models.IntegerField()),
            ],
            options={
                'ordering': ['brand', '-year', '-doors'],
            },
        ),
        migrations.CreateModel(
            name='CarInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular car', primary_key=True, serialize=False)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Car availability', max_length=1)),
                ('borrower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='loan.Car')),
            ],
            options={
                'ordering': ['due_back'],
                'permissions': (('can_mark_returned', 'Set car as returned'),),
            },
        ),
    ]
