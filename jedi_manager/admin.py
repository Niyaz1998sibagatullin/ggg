from django.contrib import admin
from .models import Planet, Jedi, Candidate, PadawanTest, Questions

admin.site.register(Jedi)
admin.site.register(Planet)
admin.site.register(Candidate)
admin.site.register(PadawanTest)
admin.site.register(Questions)

