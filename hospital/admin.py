from django.contrib import admin
from .models import Doctor, Patient, Slider, Service, Item, Expertize, Faq, Gallery

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctor, DoctorAdmin)


class PatientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)

admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Item)
admin.site.register(Expertize)
admin.site.register(Faq)
admin.site.register(Gallery)
