from django.db import models
from django.conf import settings

class InsurancePlan(models.Model):
    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20)
    age_group = models.CharField(max_length=20)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class InsuranceApplication(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='insurance_applications'
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()

    plan = models.ForeignKey(
        InsurancePlan,
        on_delete=models.CASCADE
    )
    STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    message = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name