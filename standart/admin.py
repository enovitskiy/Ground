from django.contrib import admin
from .models import Post, Category, \
    Navconstruct,Subnavigator,Text,Container,Templates,Pictures,Metka,Examples,Table,Templatecategory
from parler.admin import TranslatableStackedInline

from django.contrib.sites.models import Site

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)

admin.site.register(Text)





def duplicate_event(ModelAdmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_event.short_description = "Duplicate selected record"


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


from parler.admin import TranslatableAdmin
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)





class Text(TranslatableStackedInline):
    model = Text
    extra = 0

class Table(TranslatableStackedInline):
    model = Table
    extra = 0

class Menu(admin.StackedInline):
    model = Container
    extra = 0

class Example(TranslatableStackedInline):
    model = Examples
    extra = 0
@admin.register(Navconstruct)
class Navconstruct(TranslatableAdmin):
    filter_horizontal = ('site',)
    list_filter = ('site', )
    list_display = ['name', 'slug']
    inlines = [Example,Menu]
    actions = [duplicate_event]
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}



class SubnavigatorAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']

admin.site.register(Subnavigator, SubnavigatorAdmin)


class PicturesAdmin(TranslatableAdmin):
    fields = ['image','alt','width','height']

admin.site.register(Pictures,PicturesAdmin)

@admin.register(Container)
class Container(admin.ModelAdmin):
    list_filter = ('name',  'examples')
    inlines = [Text,Table]

admin.site.register(Templates)

class MetkaAdmin(TranslatableAdmin):
    fields = ['title']

admin.site.register(Metka,MetkaAdmin)

@admin.register(Examples)
class Examples(TranslatableAdmin):
    filter_horizontal = ('marks',)
    inlines = [Menu]


class TemplatecategoryAdmin(TranslatableAdmin):
    fields = ['name','slug','status']
admin.site.register(Templatecategory,TemplatecategoryAdmin)
