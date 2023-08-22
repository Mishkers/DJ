from django.contrib import admin
from .models import Advert

# Register your models here.


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'date_of_creation', 'updated_at', 'get_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_true', 'make_auction_as_false']
    fieldsets = (
        ("Общее", {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)



admin.site.register(Advert, AdvertAdmin)
