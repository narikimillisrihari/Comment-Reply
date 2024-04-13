from django.contrib import admin
from fbapp.models   import  Add_post,Comment
# Register your models here.
@admin.register(Add_post)

class AddAdmin(admin.ModelAdmin):
    list_display=['id','post_title','post_urls','post_comment','post_image','add_comment']

admin.site.register(Comment)