from django.contrib import admin

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_filter = ("place",)


admin.site.register(Place)
