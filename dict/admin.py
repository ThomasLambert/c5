from c5.dict.models import Reading, GtrVoicing
from django.contrib import admin


#class GtrVoicingAdmin(admin.ModelAdmin):
#    fields = ('shape', 's1', 's2', 's3', 's4', 's5', 's6')
#    list_display = ('shape', 's1', 's2', 's3', 's4', 's5', 's6')


#class ReadingAdmin(admin.ModelAdmin):
#    fields = ('pcset', )#'rname' , 'rtype', 'fondamental', 'shape', 'created')
#    list_display = ('pcset' , )#'rname' , 'rtype', 'fondamental', 'shape', 'created')



admin.site.register(Reading)




