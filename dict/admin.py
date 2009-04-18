from django.contrib import admin
from models import Cycle, Reading, GtrVoicing

class CycleAdmin(admin.ModelAdmin):
    fields = ('n1','n2')
    list_display = ('n1','n2')

class GtrVoicingAdmin(admin.ModelAdmin):
    fields = ('cycle', 's1', 's2', 's3', 's4', 's5', 's6')
    list_display = ('cycle', 's1', 's2', 's3', 's4', 's5', 's6')


class ReadingAdmin(admin.ModelAdmin):
    fields = ('rname' , 'rtype', 'fondamental', 'cycle', 'created')
    list_display = ('rname' , 'rtype', 'fondamental', 'cycle', 'created')


admin.site.register(Cycle, CycleAdmin)
admin.site.register(Reading, ReadingAdmin)
admin.site.register(GtrVoicing, GtrVoicingAdmin)
