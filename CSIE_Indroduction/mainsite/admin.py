from django.contrib import admin
from mainsite import models

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('tag','body','uploadTime')

class ProfAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug', 'title', 'description')

class CoruseAdmin(admin.ModelAdmin):
    list_display = ('name','slug','time','credit','description','sweetScale')

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name','area','description')

admin.site.register(models.News,NewsAdmin)
admin.site.register(models.Professor,ProfAdmin)
admin.site.register(models.course,CoruseAdmin)
admin.site.register(models.facility,FacilityAdmin)
