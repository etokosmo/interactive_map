from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin, \
    SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = ["get_preview"]

    def get_preview(self, image):
        return format_html(
            "<img src={} style='max-height: 200px;'>",
            image.image.url
        )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    raw_id_fields = ("place",)
    list_filter = ("place",)


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = ["title", ]
    inlines = [
        ImageInline,
    ]
