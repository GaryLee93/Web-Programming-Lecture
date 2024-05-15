from django.contrib import admin
from .models import Post,Mood,MoodPost

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date','abstract')

class MoodPostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','enabled','pub_time')
    ordering = ('-pub_time',)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Mood)
admin.site.register(MoodPost,MoodPostAdmin)
