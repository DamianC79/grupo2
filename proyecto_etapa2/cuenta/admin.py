from django.contrib import admin
from .models import Perfil,Perfil_trabajador,Titulo,Categoria,Matricula_Titulo

admin.site.register(Categoria)
admin.site.register(Perfil)
admin.site.register(Perfil_trabajador)
admin.site.register(Titulo)
admin.site.register(Matricula_Titulo)


# Register your models here.
