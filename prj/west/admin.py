from django.contrib import admin

# Register your models here.

from west.models import Character, Contact, Tag


'''
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
'''


'''
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main', { 
            'fields':('name', 'email'),
        }],
       
        ['Advance', { 
            'classes': ('collapse',),
            'fields': ('age',), 
        }] 
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Character, Tag])
'''


class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main',{
          'fields': ('name', 'email'),
        }],
        ['Advance',{
          'classes': ('collapse',),
          'fields': ('age',),
        }]  
    )
    
    list_display = ('name', 'age', 'email') 


    search_fields = ('name',)


admin.site.register(Contact, ContactAdmin)
admin.site.register([Character])


