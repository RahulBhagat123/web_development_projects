#importing relevant packages/modules
from django.contrib import admin
from .models import add_user,add_book

admin.site.register(add_book)
admin.site.register(add_user)
