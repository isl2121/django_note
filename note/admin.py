from django.contrib import admin
from .models import Note, Category, Tag
from django_summernote.admin import SummernoteModelAdmin


class Note_Admin(SummernoteModelAdmin):
    list_per_page = 20
    search_fields = ['title', 'content']
    list_display = ('title', 'content','category','created_time')
    filter_horizontal = ('tags',)
    list_filter = ('category', 'tags')
   

admin.site.register(Note, Note_Admin)
admin.site.register(Category)
admin.site.register(Tag)