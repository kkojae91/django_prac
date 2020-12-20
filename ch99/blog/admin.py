from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','slug' ,'modify_dt')
  list_filter = ('modify_dt',)
  search_fields = ('title', 'content')
  prepopulated_fields = {'slug':('title',)}
