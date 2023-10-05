# Generated by Django 3.2.21 on 2023-10-05 20:27

import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.models.fields
import nautobot.core.models.ordering
import nautobot.core.models.query_functions
import nautobot.extras.models.mixins
import nautobot.extras.models.models
import nautobot.extras.models.roles
import nautobot.extras.models.statuses
import nautobot.extras.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    replaces = [
        ("virtualization", "0001_initial"),
        ("virtualization", "0002_virtualmachine_local_context_schema"),
        ("virtualization", "0003_vminterface_verbose_name"),
        ("virtualization", "0004_auto_slug"),
        ("virtualization", "0005_add_natural_indexing"),
        ("virtualization", "0006_vminterface_status"),
        ("virtualization", "0007_vminterface_status_data_migration"),
        ("virtualization", "0008_vminterface_parent"),
        ("virtualization", "0009_cluster_location"),
        ("virtualization", "0010_vminterface_mac_address_data_migration"),
        ("virtualization", "0011_alter_vminterface_mac_address"),
        ("virtualization", "0012_alter_virtualmachine_role_add_new_role"),
        ("virtualization", "0013_migrate_virtualmachine_role_data"),
        ("virtualization", "0014_rename_virtualmachine_roles"),
        ("virtualization", "0015_rename_foreignkey_fields"),
        ("virtualization", "0016_remove_site_foreign_key_from_cluster_class"),
        ("virtualization", "0017_created_datetime"),
        ("virtualization", "0018_related_name_changes"),
        ("virtualization", "0019_vminterface_ip_addresses_m2m"),
        ("virtualization", "0020_remove_clustergroup_clustertype_slug"),
        ("virtualization", "0021_tagsfield_and_vminterface_to_primarymodel"),
        ("virtualization", "0022_vminterface_timestamps_data_migration"),
        ("virtualization", "0023_ipam__namespaces"),
        ("virtualization", "0024_fixup_null_statuses"),
        ("virtualization", "0025_status_nonnullable"),
        ("virtualization", "0026_change_virtualmachine_primary_ip_fields"),
    ]

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ipam', '0101_squashed'),
        ('dcim', '0103_link_apps'),
        ('tenancy', '0101_squashed'),
        ('extras', '0102_link_apps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('comments', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='ClusterGroup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='ClusterType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('local_config_context_data', models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True)),
                ('local_config_context_data_owner_object_id', models.UUIDField(blank=True, default=None, null=True)),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('vcpus', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('memory', models.PositiveIntegerField(blank=True, null=True)),
                ('disk', models.PositiveIntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_machines', to='virtualization.cluster')),
                ('local_config_context_data_owner_content_type', nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(blank=True, default=None, limit_choices_to=nautobot.extras.utils.FeatureQuery('config_context_owners'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='virtual_machines', to='contenttypes.contenttype')),
                ('local_config_context_schema', nautobot.core.models.fields.ForeignKeyWithAutoRelatedName(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='virtual_machines', to='extras.configcontextschema')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='virtual_machines', to='dcim.platform')),
                ('primary_ip4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ipam.ipaddress')),
                ('primary_ip6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='ipam.ipaddress')),
                ('role', nautobot.extras.models.roles.RoleField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='virtual_machines', to='extras.role')),
                ('status', nautobot.extras.models.statuses.StatusField(on_delete=django.db.models.deletion.PROTECT, related_name='virtual_machines', to='extras.status')),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='virtual_machines', to='tenancy.tenant')),
            ],
            options={
                'ordering': ('name',),
                'unique_together': {('cluster', 'tenant', 'name')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin, nautobot.extras.models.models.ConfigContextSchemaValidationMixin),
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to='virtualization.clustergroup'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to='virtualization.clustertype'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to='dcim.location'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='tags',
            field=nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='tenant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clusters', to='tenancy.tenant'),
        ),
        migrations.CreateModel(
            name='VMInterface',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('_custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('enabled', models.BooleanField(default=True)),
                ('mac_address', nautobot.core.models.fields.MACAddressCharField(blank=True, default='')),
                ('mtu', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(65536)])),
                ('mode', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(db_index=True, max_length=64)),
                ('_name', nautobot.core.models.fields.NaturalOrderingField('name', blank=True, db_index=True, max_length=100, naturalize_function=nautobot.core.models.ordering.naturalize_interface)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('bridge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bridged_interfaces', to='virtualization.vminterface')),
                ('ip_addresses', models.ManyToManyField(blank=True, related_name='vm_interfaces', through='ipam.IPAddressToInterface', to='ipam.IPAddress')),
                ('parent_interface', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_interfaces', to='virtualization.vminterface')),
                ('status', nautobot.extras.models.statuses.StatusField(on_delete=django.db.models.deletion.PROTECT, related_name='vm_interfaces', to='extras.status')),
                ('tagged_vlans', models.ManyToManyField(blank=True, related_name='vminterfaces_as_tagged', to='ipam.VLAN')),
                ('tags', nautobot.core.models.fields.TagsField(through='extras.TaggedItem', to='extras.Tag')),
                ('untagged_vlan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vminterfaces_as_untagged', to='ipam.vlan')),
                ('virtual_machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='virtualization.virtualmachine')),
                ('vrf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vm_interfaces', to='ipam.vrf')),
            ],
            options={
                'verbose_name': 'VM interface',
                'ordering': ('virtual_machine', nautobot.core.models.query_functions.CollateAsChar('_name')),
                'unique_together': {('virtual_machine', 'name')},
            },
            bases=(models.Model, nautobot.extras.models.mixins.DynamicGroupMixin, nautobot.extras.models.mixins.NotesMixin),
        ),
    ]
