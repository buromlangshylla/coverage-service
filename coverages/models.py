from django.db import models
import uuid


class Base(models.Model):
    created_by = models.CharField(max_length=250, editable=False, null=True, blank=True)
    modified_by = models.CharField(max_length=250, editable=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Coverage(Base):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    eligibility_criteria = models.TextField(blank=True, null=True)
    max_coverage_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.name} ({self.status})"


class CustomerCoverage(Base):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_id = models.UUIDField()
    policy_id = models.UUIDField(blank=True, null=True)
    coverage = models.ForeignKey(Coverage, on_delete=models.CASCADE, related_name='customer_coverages')
    effective_date = models.DateField()
    expiry_date = models.DateField()
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"CustomerCoverage {self.id} for customer {self.customer_id}"
