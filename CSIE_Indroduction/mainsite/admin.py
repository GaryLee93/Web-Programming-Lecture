from django.contrib import admin
from .models import News, Professor

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('tag','body','uploadTime')

class ProfAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'title', 'description')

admin.site.register(News,NewsAdmin)
admin.site.register(Professor,ProfAdmin)
