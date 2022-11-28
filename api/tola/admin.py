from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(user_gym)
admin.site.register(Gym)
admin.site.register(Exercise)
admin.site.register(Max)

# Register your models here.
