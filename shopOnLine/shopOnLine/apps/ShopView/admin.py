from django.contrib import admin

from .models import product, Comment, user

admin.site.register(product)
admin.site.register(Comment)
admin.site.register(user)