from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.utils.html import format_html

from .models import Place, Image


class LimitModelFormset(BaseInlineFormSet):
    """ Base Inline formset to limit inline Model query results. """

    def __init__(self, *args, **kwargs):
        super(LimitModelFormset, self).__init__(*args, **kwargs)
        _kwargs = {self.fk.name: kwargs['instance']}
        self.queryset = kwargs['queryset'].filter(**_kwargs).order_by(
            '-order')[
                        :5]


class ImageInline(admin.TabularInline):
    # formset = LimitModelFormset
    model = Image
    readonly_fields = ["get_preview"]
    fields = ('image', 'get_preview', 'order')

    def get_preview(self, image):
        return format_html(
            f"<img src={image.image.url} style='max-height: 200px;'>",
        )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("place",)
    list_filter = ("place",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
