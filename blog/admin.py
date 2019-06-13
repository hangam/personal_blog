from django.contrib import admin
from .models import Blog
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm
from .models import User, Blog, Contact, Category

# class CustomUserAdmin(UserAdmin):
# 	add_form = CustomUser
# 	model = CustomUser
# 	# list_display = ['email']

admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Category)
