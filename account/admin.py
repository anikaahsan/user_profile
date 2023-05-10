from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account





# Register your models here.
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display=['id','email','first_name','last_name','last_login','date_joined','is_active']
    readonly_fields=['date_joined','last_login']
    
    filter_horizontal=()
    list_filter=()
    fieldsets=[]
