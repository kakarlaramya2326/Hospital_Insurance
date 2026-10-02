from django.db import models


class InsurancePlan(models.Model):
    PLAN_TYPES = [
        ('Basic', 'Basic'),
        ('Medium', 'Medium'),
        ('Premium', 'Premium'),
    ]

    AGE_GROUPS = [
        ('0-6', '0-6 Years'),
        ('6-12', '6-12 Years'),
        ('12+', '12+ Years'),
    ]

    name = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUPS)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.age_group}"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name


class InsurancePolicy(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(InsurancePlan, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.policy_number

