from django.contrib import admin
from.models import EmpresaDB, OfertaDB,ResenasDB, Habilidades, UsuarioPersonalizado

# Register your models here.

admin.site.register(UsuarioPersonalizado)
admin.site.register(EmpresaDB)     
admin.site.register(Habilidades)
admin.site.register(OfertaDB)
admin.site.register(ResenasDB)

