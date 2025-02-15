from django.contrib import admin
from .models import Reg

class AdminReg(admin.ModelAdmin):
    list_display = ['username','email']

admin.site.register(Reg,AdminReg)
