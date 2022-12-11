from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(user_gym)
admin.site.register(Gym)
admin.site.register(Exercise)
admin.site.register(Max)
admin.site.register(Program)
admin.site.register(user_program)
admin.site.register(program_session)
admin.site.register(program_session_exercise)
admin.site.register(program_session_exercise_set)
admin.site.register(user_set)

# Register your models here.
