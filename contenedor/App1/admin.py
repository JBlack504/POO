from django.contrib import admin
from.models import EmpresaDB, OfertaDB,ResenasDB, Habilidades, UsuarioPersonalizado


# Register your models here.
#admin.site.register(UsuarioDB)
admin.site.register(UsuarioPersonalizado)
admin.site.register(EmpresaDB)     
admin.site.register(Habilidades)
admin.site.register(OfertaDB)
admin.site.register(ResenasDB)


#class OfertaAdmin(admin.ModelAdmin):
   # list_display = ('titulo', 'empleador', 'topicos')
   # search_fields = ('titulo', 'descripcion')
   # list_filter = ('topicos')






