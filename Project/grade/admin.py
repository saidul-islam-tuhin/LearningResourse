from django.contrib import admin
#from .models import Subject,Student,Point

# Register your models here.
"""class Studen_admin(admin.ModelAdmin):
    list_display = ('std_name',)
    search_fields = ['std_id',]
    filter_horizontal = ('members',)

class point_admin(admin.ModelAdmin):
    list_display = ('sub_name',)
    search_fields = ['std_id',]
    #filter_horizontal = ('std_id','sub_name',)

admin.site.register(Subject)
admin.site.register(Student,Studen_admin)
admin.site.register(Point,point_admin)
class Amenity_admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name',]
    #filter_horizontal = ('members',)

class Store_admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['city',]
    filter_horizontal = ('amenities',)


admin.site.register(Amenity,Amenity_admin)
admin.site.register(Store,Store_admin)"""