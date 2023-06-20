# Generated by Django 3.2.18 on 2023-05-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0031_ipam___data_migrations"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vrf",
            unique_together={("namespace", "rd")},
        ),
        migrations.AlterUniqueTogether(
            name="prefix",
            unique_together={("namespace", "network", "prefix_length")},
        ),
        migrations.AlterUniqueTogether(
            name="ipaddress",
            unique_together={("parent", "host")},
        ),
        migrations.RemoveField(
            model_name="ipaddress",
            name="broadcast",
        ),
        migrations.RemoveField(
            model_name="ipaddress",
            name="vrf",
        ),
        migrations.RenameField(
            model_name="ipaddress",
            old_name="prefix_length",
            new_name="mask_length",
        ),
        migrations.AlterModelOptions(
            name="ipaddress",
            options={
                "ordering": ("ip_version", "host", "mask_length"),
                "verbose_name": "IP address",
                "verbose_name_plural": "IP addresses",
            },
        ),
        migrations.RemoveField(
            model_name="prefix",
            name="vrf",
        ),
        migrations.RemoveField(
            model_name="vrf",
            name="enforce_unique",
        ),
        migrations.RenameField(
            model_name="vrf",
            old_name="prefixes_m2m",
            new_name="prefixes",
        ),
        migrations.AlterField(
            model_name="vrf",
            name="prefixes",
            field=models.ManyToManyField(related_name="vrfs", through="ipam.VRFPrefixAssignment", to="ipam.Prefix"),
        ),
    ]
