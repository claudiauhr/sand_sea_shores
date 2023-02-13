from django.contrib import admin
from .models import Shore, Reservation, Attraction, Image


class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(Image, imageAdmin)

admin.site.register(Shore)
admin.site.register(Attraction)
admin.site.register(Reservation)
