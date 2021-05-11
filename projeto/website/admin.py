from django.contrib import admin
from .models import Automato, ExpressaoRegular, MaquinaTuring

# Register your models here.

admin.site.register(Automato)
admin.site.register(ExpressaoRegular)
admin.site.register(MaquinaTuring)