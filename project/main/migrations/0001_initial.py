# Generated by Django 5.0 on 2023-12-12 15:53

import django.db.models.deletion
import project.main.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True, null=True)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("archived", models.DateTimeField()),
                (
                    "action_date",
                    models.IntegerField(
                        validators=[project.main.models.validate_due_date]
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("BILL", "Bill"),
                            ("SAVING", "Saving"),
                            ("TRANSFER", "Transfer"),
                        ],
                        max_length=50,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        validators=[project.main.models.validate_more_than_zero],
                    ),
                ),
                (
                    "source_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source",
                        to="main.account",
                    ),
                ),
                (
                    "target_account",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target",
                        to="main.account",
                    ),
                ),
            ],
            options={
                "ordering": ["-action_date"],
            },
        ),
    ]
