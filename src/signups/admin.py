from django.contrib import admin

# Register your models here.
from .models import SighUp, Patient


class PatientAdmin(admin.ModelAdmin):
    class Meta:
        model = Patient
        
class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model = SighUp
        
admin.site.register(SighUp, SignUpAdmin)
        
admin.site.register(Patient, PatientAdmin)