from django.contrib import admin

# Register your models here.
from .models import Construccion
@admin.register(Construccion)
class ConstruccionAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'get_materiales_list', 'descripcion')
  search_fields = ('nombre',)
  

