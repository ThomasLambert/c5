from c5.dict.models import Shape, Reading, GtrVoicing
from django.contrib import admin


class ShapeAdmin(admin.ModelAdmin):
    fields = 'shape_id'
    list_display = 'shape_id'

#class GtrVoicingAdmin(admin.ModelAdmin):
#    fields = ('shape', 's1', 's2', 's3', 's4', 's5', 's6')
#    list_display = ('shape', 's1', 's2', 's3', 's4', 's5', 's6')


#class ReadingAdmin(admin.ModelAdmin):
#    fields = ('rname' , 'rtype', 'fondamental', 'shape', 'created')
#    list_display = ('rname' , 'rtype', 'fondamental', 'shape', 'created')


admin.site.register(Shape, ShapeAdmin)

