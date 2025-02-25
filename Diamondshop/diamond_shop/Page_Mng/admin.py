from django.contrib import admin
from .models  import User
# Register your models here.
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

class UserMng(admin.ModelAdmin):
  list_display = ("name", "email", "birth_date",)
  
admin.site.register(User, UserMng)