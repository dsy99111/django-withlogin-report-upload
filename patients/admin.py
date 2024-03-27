# admin.py
from django.contrib import admin
from .models import Patient, TestReport

class TestReportAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "patient":
            # Limit the choices for 'patient' to only those patients associated with users
            kwargs["queryset"] = Patient.objects.filter(user__isnull=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Patient)
admin.site.register(TestReport, TestReportAdmin)
