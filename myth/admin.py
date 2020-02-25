from django.contrib import admin
from .models import Region, Type, Being, Relation, God_Of, Story, FaveGod, FaveStory
# Register your models here.

admin.site.register(Region)
admin.site.register(Type)
admin.site.register(Being)
admin.site.register(Relation)
admin.site.register(God_Of)
admin.site.register(Story)
admin.site.register(FaveGod)
admin.site.register(FaveStory)