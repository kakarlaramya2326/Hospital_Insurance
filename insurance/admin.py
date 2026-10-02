from django.contrib import admin
from .models import InsurancePlan, InsuranceApplication, ContactMessage


@admin.register(InsurancePlan)
class InsurancePlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'plan_type',
        'age_group',
        'premium',
        'coverage',
    )

    list_filter = (
        'plan_type',
        'age_group',
    )

    search_fields = (
        'name',
        'plan_type',
        'age_group',
    )


@admin.register(InsuranceApplication)
class InsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = (
    'user',
    'full_name',
    'email',
    'phone',
    'date_of_birth',
    'plan',
    'status',
    'applied_on',
    
)
    list_editable = ('status',)
    list_filter = (
        'plan',
        'status',
        'applied_on',
    )

    search_fields = (
        'user__username',
        'user__email',
        'full_name',
        'email',
        'phone',
    )

    readonly_fields = (
        'applied_on',
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'sent_on',
    )

    search_fields = (
        'name',
        'email',
        'phone',
    )

    readonly_fields = (
        'sent_on',
    )