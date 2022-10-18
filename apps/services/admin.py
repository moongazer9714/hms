from django.contrib import admin
from .models import Rent,Car,Cat
# Register your models here.
admin.site.register(Cat)
admin.site.register(Car)
admin.site.register(Rent)