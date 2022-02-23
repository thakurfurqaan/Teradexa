from django.contrib import admin
from .models import Post, UserRegistrationModel

# Register your models here.

admin.site.register(UserRegistrationModel)
admin.site.register(Post)
