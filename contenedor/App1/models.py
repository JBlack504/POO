from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.  
class UsuarioDB(models.Model):
    nombre = models.CharField(max_length=50, null=False, verbose_name="Nombre", blank=False)
    
    class Meta:
        db_table = "Usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return self.nombre

class UsuarioPersonalizado(AbstractUser):
    usuabiodb = models.ForeignKey(UsuarioDB,on_delete=models.CASCADE, null=True, blank=False,)

    class Meta:
        db_table='Usuario'
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'

    def save(self, *args, **kwargs):
        # Verificar si la contraseña no está encriptada
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class EmpleadorDB(models.Model):
       nombre_empresa = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nombre de Empresa")
       descripcion = models.TextField(max_length=400, null=False, verbose_name="Descripcion")
       
       
       class Meta:
        db_table = "Empleadores"
        verbose_name = "Empleador"
        verbose_name_plural = "Empleadores"
        
       def __str__(self):
           return self.nombre_empresa
       
class Habilidades(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False,verbose_name="nombre")
    
    class Meta:
        db_table = "Habilidades"
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        
    def __str__(self):
           return self.nombre
       
       
class OfertaDB(models.Model):
    
    topicos_choises = (
        ('PR','Programacion'),
        ('SG','Seguridad'),
        ('IA', 'Inteligencia Artificial'),
    )
    
    empleador = models.ForeignKey(EmpleadorDB, on_delete=models.CASCADE )
    titulo = models.CharField(max_length=50, null=False, blank=False, verbose_name="Titulo")
    descripcion = models.TextField(null=False, blank=False, verbose_name="Descripcion")
    Habilidades = models.ForeignKey( Habilidades,max_length=50, null=True, verbose_name="Habilidades", on_delete=models.CASCADE)
    topicos = models.CharField(max_length=100, verbose_name='Topicos', choices=topicos_choises)
    beneficios = models.TextField(verbose_name="Beneficios")
    
    
    class Meta:
        db_table = "Ofertas"
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"
    
    def __str__(self):
           return self.titulo
    
class ResenasDB(models.Model):
    usuario = models.ForeignKey(UsuarioDB, null=True,on_delete=models.CASCADE )
    contenido = models.TextField(verbose_name="Contenido", null=False, blank=True)
    calificacion = models.CharField( max_length= 10 ,verbose_name="Calificación", 
        validators=[
            MinValueValidator(0),  # Valor mínimo 0
            MaxValueValidator(10) # Valor máximo 10
        ])
    
    class Meta:
        db_table = "Reseñas"
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        
    def __str__(self):
           return self.id