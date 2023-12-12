import uuid

from django.db import models


def validate_due_date(value):
    if 1 <= value <= 31:
        return True
    return False


def validate_more_than_zero(value):
    if value < 0:
        return True
    return False


class Payment(models.Model):
    class Type(models.TextChoices):
        BILL = "BILL", ("bill")
        SAVING = "SAVING", ("saving")
        TRANSFER = "TRANSFER", ("transfer")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)
    archived = models.DateTimeField(null=True)
    action_date = models.IntegerField(validators=[validate_due_date])

    type = models.CharField(max_length=20, choices=Type.choices)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[validate_more_than_zero]
    )

    source_account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, related_name="source"
    )
    target_account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, null=True, related_name="target"
    )

    class Meta:
        ordering = ["-action_date"]

    def __str__(self):
        return f"{self.source_account} {self.amount} => {self.target_account if self.target_account else 'EXTERNAL'}"


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    is_active = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name}"


# class Transaction(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created = models.DateTimeField(auto_now_add=True, db_index=True)
#     modified = models.DateTimeField(auto_now=True)

#     class Type(models.TextChoices):
#         BILL = "BILL", ("Bill")
#         SAVING = "SAVING", ("Saving")
#         TRANSFER = "TRANSFER", ("Transfer")

#     summary = models.CharField(max_length=300)
#     type = models.CharField(max_length=50, choices=Type.choices)
#     due_date = models.IntegerField(validators=[validate_due_date])
#     amount = models.DecimalField(max_digits=4, decimal_places=2)

#     source_account = models.ForeignKey(
#         "Account", on_delete=models.CASCADE, null=True, related_name="source"
#     )
#     target_account = models.ForeignKey(
#         "Account", on_delete=models.CASCADE, null=True, related_name="target"
#     )
#     payment = models.ForeignKey("Payment", on_delete=models.CASCADE)

#     class Meta:
#         ordering = ["-created"]

#     def __str__(self):
#         return f"{self.source_account} {self.payment.amount} => {self.target_account if self.target_account else 'EXTERNAL'}"
