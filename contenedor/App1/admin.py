from django.contrib import admin
from.models import UsuarioDB, EmpleadorDB, OfertaDB,ResenasDB, Habilidades, UsuarioPersonalizado


# Register your models here.
#class UsuarioAdmin(admin.ModelAdmin):
    #fields = ["nombre","edad","correo", "contrasena"]
    #list_display = ["nombre", "correo"]
    
admin.site.register(UsuarioDB)

admin.site.register(UsuarioPersonalizado)
    
    
class EmpleadorAdmin(admin.ModelAdmin):
    fields = ["nombre_empresa", "descripcion"]
    list_display = ["nombre_empresa"]
admin.site.register(EmpleadorDB, EmpleadorAdmin)

class HabilidadesAdmin(admin.ModelAdmin):
    fields = ["nombre"]
admin.site.register(Habilidades, HabilidadesAdmin)

#class OfertaAdmin(admin.ModelAdmin):
    #fields = ["empleador","titulo", "descripcion", "Habilidades", "topicos", "beneficios"]
admin.site.register(OfertaDB)








