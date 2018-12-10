from django.contrib import admin
from .models import Guestbook

class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','pub_date')

admin.site.register(Guestbook,GuestbookAdmin)
