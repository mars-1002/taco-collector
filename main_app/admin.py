from django.contrib import admin
from .models import Taco, Feeding, Sauce

# Register your models here.
admin.site.register(Taco)
admin.site.register(Feeding)
admin.site.register(Sauce)