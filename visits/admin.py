from django.contrib import admin
from .models import Visitors,Order,Profile

class Menu(admin.StackedInline):
    model = Order
    extra = 0

class VisitorsAdmin(admin.ModelAdmin):
    list_display = ['Login','__str__', 'IP', 'num_visits','Location',
                    ]
    inlines = [Menu]
    list_filter = ['IP', 'num_visits', 'useragent']

admin.site.register(Visitors, VisitorsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'email', 'city', 'metka','created',
                    ]

    list_filter = ['created','lead']


admin.site.register(Order, OrderAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile, ProfileAdmin)