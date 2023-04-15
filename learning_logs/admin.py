from django.contrib import admin

# Register your models here.
# The dot before models tells Django to look for models.py in the same directory
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
