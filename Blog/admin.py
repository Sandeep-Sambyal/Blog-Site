from django.contrib import admin
from .models import    blogpost,Blogcomment

# Register your models here.
admin.site.register((Blogcomment))


@admin.register(blogpost)
class blogpostAdmin(admin.ModelAdmin):
    class Media:
        js=('blog/tinyJS.js',)