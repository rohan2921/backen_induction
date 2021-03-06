# Generated by Django 3.2.3 on 2021-06-02 09:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('lp_number', models.IntegerField(blank=True, null=True)),
                ('wheel_count', models.IntegerField(choices=[(4, 4), (6, 6), (8, 8), (10, 10)], default=None)),
                ('manufacturer', models.CharField(default=None, max_length=25)),
                ('model_name', models.CharField(default=None, max_length=25)),
                ('vehicle_price', models.IntegerField(default=0)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('grey', 'Grey'), ('white', 'White'), ('black', 'Black')], default=None, max_length=25)),
            ],
            options={
                'ordering': ['vehicle_price'],
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=40, null=True)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RandomEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_city', models.CharField(default=None, max_length=25)),
                ('to_city', models.CharField(default=None, max_length=25)),
                ('purpose', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShowRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('abstractvehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.abstractvehicle')),
                ('is_air_conditioned', models.BooleanField(default=True)),
                ('open_top', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['model_name'],
            },
            bases=('vehicles.abstractvehicle',),
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('abstractvehicle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.abstractvehicle')),
                ('max_capacity', models.IntegerField(default=0)),
            ],
            bases=('vehicles.abstractvehicle',),
        ),
        migrations.AddIndex(
            model_name='randomentries',
            index=models.Index(condition=models.Q(('flag__gt', 400)), fields=['flag'], name='random_search_index'),
        ),
        migrations.AddField(
            model_name='truck',
            name='c_book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='vehicles.cbook'),
        ),
        migrations.AddField(
            model_name='truck',
            name='services',
            field=models.ManyToManyField(blank=True, to='vehicles.Service'),
        ),
        migrations.AddField(
            model_name='truck',
            name='works_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.shippingagency'),
        ),
        migrations.AddField(
            model_name='showroom',
            name='truck_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.truck'),
        ),
        migrations.AddField(
            model_name='car',
            name='my_bills',
            field=models.ManyToManyField(blank=True, to='vehicles.Bill'),
        ),
        migrations.AlterUniqueTogether(
            name='truck',
            unique_together={('max_capacity', 'works_for')},
        ),
    ]
