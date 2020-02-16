from django.contrib import admin
from .models import Region, Type, Being, Relation
# Register your models here.

admin.site.register(Region)
admin.site.register(Type)
admin.site.register(Being)
admin.site.register(Relation)