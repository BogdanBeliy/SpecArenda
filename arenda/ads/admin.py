from django.contrib import admin
from .models import *

admin.site.register(OrganisationContacts)



@admin.register(Organization)
class OrganisationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ChildCatInline(admin.TabularInline):
    model = ChildCategory
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PaprentCategory)
class ParentCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',]
    inlines = [ChildCatInline]
    
@admin.register(ChildCategory)
class ChildCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category']


@admin.register(Region)
class RegionnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'created', 'updated', 'draft']



