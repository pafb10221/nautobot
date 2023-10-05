# Generated by Django 3.2.21 on 2023-10-05 20:27

from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.models.fields


class Migration(migrations.Migration):

    initial = True

    replaces = [
        ("dcim", "0002_initial_part_2"),
        ("dcim", "0012_interface_parent_bridge"),
        ("dcim", "0013_location_location_type"),
        ("dcim", "0032_rename_foreignkey_fields"),
        ("dcim", "0042_alter_location_managers"),
        ("dcim", "0049_remove_slugs_and_change_device_primary_ip_fields"),
    ]

    dependencies = [
        ('tenancy', '0101_squashed'),
        ('dcim', '0101_squashed'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('extras', '0101_squashed'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualchassis',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='rearporttemplate',
            name='device_type',
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(on_delete=django.db.models.deletion.CASCADE, related_name='rear_port_templates', to='dcim.devicetype'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='_cable_peer_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='cable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.cable'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='device',
            field=nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(on_delete=django.db.models.deletion.CASCADE, related_name='rear_ports', to='dcim.device'),
        ),
        migrations.AddField(
            model_name='rearport',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='rack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rack_reservations', to='dcim.rack'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='rackreservation',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rack_reservations', to='tenancy.tenant'),
        ),
    ]
