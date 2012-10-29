from django.contrib import admin

from . import models

class MemberAdmin(admin.ModelAdmin):
    list_display = ['email', 'signup_time', 'is_subscribed']
    list_filter = ['is_subscribed']
    date_hierarchy = 'signup_time'

admin.site.register(models.Member, MemberAdmin)
