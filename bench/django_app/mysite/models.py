from django.db import models


class Record(models.Model):
    summary = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    project = models.CharField(max_length=16)
    region = models.CharField(max_length=8, db_index=True)
    total_budget = models.FloatField(null=True)
    info = models.CharField(max_length=128)
    purpose = models.CharField(max_length=256)
    department = models.CharField(max_length=256)
    business = models.TextField(blank=False)
    is_budget = models.BooleanField()
    customer = models.CharField(max_length=128, blank=False)
    owner = models.CharField(max_length=128, blank=False)
    approved_by = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True)
    closed = models.BooleanField(default=False)

