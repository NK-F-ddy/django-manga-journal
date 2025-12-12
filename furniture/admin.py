# furniture/admin.py

from django.contrib import admin
from .models import Item, RoomImage

admin.site.register(Item)
admin.site.register(RoomImage)
