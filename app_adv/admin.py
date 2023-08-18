from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'make_auction_true']
    fieldsets = (
        ("Общие", {
            'fields': ('title', 'description')
        }),
        ("Финансы", {
            'fields': ('price', 'auction'),
            'classes': ('collapse',),
        })
    )
    @admin.action(description='Закрыть торг')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Открыть торг')
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)