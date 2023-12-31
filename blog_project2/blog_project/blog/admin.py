from django.contrib import admin
from .models import Category,Post
# Register your models here.

class CateogoryAdmin(admin.ModelAdmin):
    list_display = ['image_tag','title','description','url','add_date']
    search_fields = ['title']
    list_per_page = 5
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['cat']
    list_per_page = 5
    class Media:
        js = ('js/script.js',)

admin.site.register(Category,CateogoryAdmin)
admin.site.register(Post,PostAdmin)
