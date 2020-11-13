from django.contrib import admin

# Register your models here.
from django.db import models
from martor.widgets import AdminMartorWidget
from martor.models import MartorField
from stk_app.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    formfield_overrides = {
        MartorField: {'widget': AdminMartorWidget},
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post, PostAdmin)
