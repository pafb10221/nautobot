# Generated by Django 3.2.21 on 2023-10-05 20:27

from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.models.fields
import nautobot.extras.models.roles
import nautobot.extras.models.statuses
import nautobot.ipam.models


class Migration(migrations.Migration):

    initial = True

    replaces = [
        ("ipam", "0002_initial_part_2"),
        ("ipam", "0006_ipaddress_nat_outside_list"),
        ("ipam", "0008_prefix_vlan_vlangroup_location"),
        ("ipam", "0010_alter_ipam_role_add_new_role"),
        ("ipam", "0011_migrate_ipam_role_data"),
        ("ipam", "0012_rename_ipam_roles"),
        ("ipam", "0013_delete_role"),
        ("ipam", "0014_rename_foreign_keys_and_related_names"),
        ("ipam", "0018_remove_site_foreign_key_from_ipam_models"),
        ("ipam", "0020_related_name_changes"),
        ("ipam", "0021_prefix_add_rir_and_date_allocated"),
        ("ipam", "0022_aggregate_to_prefix_data_migration"),
        ("ipam", "0023_delete_aggregate"),
        ("ipam", "0024_interface_to_ipaddress_m2m"),
        ("ipam", "0025_interface_ipaddress_m2m_data_migration"),
        ("ipam", "0026_ipaddress_remove_assigned_object"),
        ("ipam", "0028_tagsfield"),
        ("ipam", "0029_ip_address_to_interface_uniqueness_constraints"),
        ("ipam", "0030_ipam__namespaces"),
        ("ipam", "0031_ipam___data_migrations"),
        ("ipam", "0032_ipam__namespaces_finish"),
        ("ipam", "0033_fixup_null_statuses"),
        ("ipam", "0034_status_nonnullable"),
        ("ipam", "0035_ensure_all_services_fit_uniqueness_constraint"),
        ("ipam", "0036_add_uniqueness_constraints_to_service"),
    ]

    dependencies = [
        ('ipam', '0101_squashed'),
        ('virtualization', '0101_squashed'),
        ('dcim', '0103_link_apps'),
        ('tenancy', '0101_squashed'),
        ('extras', '0102_link_apps'),
    ]

    operations = [
        migrations.AddField(
            model_name='vrfdeviceassignment',
            name='virtual_machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vrf_assignments', to='virtualization.virtualmachine'),
        ),
        migrations.AddField(
            model_name='vrfdeviceassignment',
            name='vrf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_assignments', to='ipam.vrf'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='devices',
            field=models.ManyToManyField(related_name='vrfs', through='ipam.VRFDeviceAssignment', to='dcim.Device'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='export_targets',
            field=models.ManyToManyField(blank=True, related_name='exporting_vrfs', to='ipam.RouteTarget'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='import_targets',
            field=models.ManyToManyField(blank=True, related_name='importing_vrfs', to='ipam.RouteTarget'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='namespace',
            field=models.ForeignKey(default=nautobot.ipam.models.get_default_namespace_pk, on_delete=django.db.models.deletion.PROTECT, related_name='vrfs', to='ipam.namespace'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='prefixes',
            field=models.ManyToManyField(related_name='vrfs', through='ipam.VRFPrefixAssignment', to='ipam.Prefix'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vrfs', to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='vrf',
            name='virtual_machines',
            field=models.ManyToManyField(related_name='vrfs', through='ipam.VRFDeviceAssignment', to='virtualization.VirtualMachine'),
        ),
        migrations.AddField(
            model_name='vlangroup',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlan_groups', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='role',
            field=nautobot.extras.models.roles.RoleField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='extras.role'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='status',
            field=nautobot.extras.models.statuses.StatusField(on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='extras.status'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='vlan',
            name='vlan_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vlans', to='ipam.vlangroup'),
        ),
        migrations.AddField(
            model_name='service',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='dcim.device'),
        ),
        migrations.AddField(
            model_name='service',
            name='ip_addresses',
            field=models.ManyToManyField(blank=True, related_name='services', to='ipam.IPAddress'),
        ),
        migrations.AddField(
            model_name='service',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='service',
            name='virtual_machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='virtualization.virtualmachine'),
        ),
        migrations.AddField(
            model_name='routetarget',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='routetarget',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='route_targets', to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='namespace',
            field=models.ForeignKey(default=nautobot.ipam.models.get_default_namespace_pk, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='ipam.namespace'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='ipam.prefix'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='rir',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='ipam.rir'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='role',
            field=nautobot.extras.models.roles.RoleField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='extras.role'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='status',
            field=nautobot.extras.models.statuses.StatusField(on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='extras.status'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='tenancy.tenant'),
        ),
        migrations.AddField(
            model_name='prefix',
            name='vlan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='prefixes', to='ipam.vlan'),
        ),
        migrations.AddField(
            model_name='namespace',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='namespaces', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='namespace',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='ipaddresstointerface',
            name='interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ip_address_assignments', to='dcim.interface'),
        ),
        migrations.AddField(
            model_name='ipaddresstointerface',
            name='ip_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ipam.ipaddress'),
        ),
        migrations.AddField(
            model_name='ipaddresstointerface',
            name='vm_interface',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ip_address_assignments', to='virtualization.vminterface'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='nat_inside',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nat_outside_list', to='ipam.ipaddress'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ip_addresses', to='ipam.prefix'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='role',
            field=nautobot.extras.models.roles.RoleField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ip_addresses', to='extras.role'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='status',
            field=nautobot.extras.models.statuses.StatusField(on_delete=django.db.models.deletion.PROTECT, related_name='ip_addresses', to='extras.status'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ip_addresses', to='tenancy.tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='vrfprefixassignment',
            unique_together={('vrf', 'prefix')},
        ),
        migrations.AlterUniqueTogether(
            name='vrfdeviceassignment',
            unique_together={('vrf', 'device'), ('vrf', 'virtual_machine')},
        ),
        migrations.AlterUniqueTogether(
            name='vrf',
            unique_together={('namespace', 'rd')},
        ),
        migrations.AlterUniqueTogether(
            name='vlan',
            unique_together={('vlan_group', 'vid'), ('vlan_group', 'name')},
        ),
        migrations.AddConstraint(
            model_name='service',
            constraint=models.UniqueConstraint(fields=('name', 'device'), name='unique_device_service_name'),
        ),
        migrations.AddConstraint(
            model_name='service',
            constraint=models.UniqueConstraint(fields=('name', 'virtual_machine'), name='unique_virtual_machine_service_name'),
        ),
        migrations.AlterUniqueTogether(
            name='prefix',
            unique_together={('namespace', 'network', 'prefix_length')},
        ),
        migrations.AlterIndexTogether(
            name='prefix',
            index_together={('network', 'broadcast', 'prefix_length'), ('namespace', 'network', 'broadcast', 'prefix_length')},
        ),
        migrations.AlterUniqueTogether(
            name='ipaddresstointerface',
            unique_together={('ip_address', 'vm_interface'), ('ip_address', 'interface')},
        ),
        migrations.AlterUniqueTogether(
            name='ipaddress',
            unique_together={('parent', 'host')},
        ),
    ]
