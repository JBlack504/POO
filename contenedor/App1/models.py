from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from datetime import date

# Create your models here.  
class UsuarioPersonalizado(AbstractUser):
    nombre = models.CharField(max_length=50, null=False, verbose_name="Nombre", blank=False)
    correo = models.EmailField(max_length=254, null=False, unique=True, verbose_name="Correo Electrónico", blank=False)
    
    class Meta:
        db_table='Usuario'
        verbose_name= 'Usuario'
        verbose_name_plural= 'Usuarios'

    def __str__(self):
        return self.nombre
    
class EmpresaDB(models.Model):
       nombre_empresa = models.CharField(max_length=40, null=False, blank=False, verbose_name="Nombre de Empresa")
       descripcion = models.TextField(null=False, verbose_name="Descripcion")
       
       
       
       class Meta:
        db_table = "Empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        
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
        ('BD', 'Bases de Datos'),
        ('DW', 'Diseño Web')
    )
    
    empleador = models.ForeignKey(EmpresaDB, on_delete=models.CASCADE )
    titulo = models.CharField(max_length=50, null=False, blank=False, verbose_name="Titulo")
    descripcion = models.TextField(null=False, blank=False, verbose_name="Descripcion")
    habilidades = models.ForeignKey( Habilidades,max_length=50, null=True, verbose_name="Habilidades", on_delete=models.CASCADE)
    topicos = models.CharField(max_length=100, verbose_name='Topicos', choices=topicos_choises)
    beneficios = models.TextField(verbose_name="Beneficios")
    promedio_calificacion = models.FloatField(verbose_name="Calificación Promedio")
    fecha_limite = models.DateField(verbose_name="Fecha Límite", null=False, blank=False, default=date.today)
    
    class Meta:
        db_table = "Ofertas"
        verbose_name = "Oferta"
        verbose_name_plural = "Ofertas"
    
    def __str__(self):
           return self.titulo
       
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
       
class ResenasDB(models.Model):
    usuario = models.ForeignKey(UsuarioPersonalizado, null=True,on_delete=models.CASCADE )
    empresa = models.ForeignKey(EmpresaDB, null=True, on_delete=models.CASCADE )
    contenido = models.TextField(verbose_name="Contenido", null=False, blank=True)
    calificacion = models.IntegerField(verbose_name="Calificación", 
        validators=[
            MinValueValidator(0),  # Valor mínimo 0
            MaxValueValidator(10) # Valor máximo 10
        ])
    
    class Meta:
        db_table = "Reseñas"
        verbose_name = "Reseña"
        verbose_name_plural = "Reseñas"
        
    def __str__(self):
          return f"Reseña de {self.usuario.nombre} - Calificación: {self.calificacion}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Actualizar el promedio de calificaciones de la oferta relacionada con la empresa
        self.actualizar_promedio_oferta()
    
    
    def actualizar_promedio_oferta(self):
        # Obtener todas las reseñas de la empresa asociada a la oferta
        ofertas = OfertaDB.objects.filter(empleador=self.empresa)
        
        for oferta in ofertas:
            reseñas = ResenasDB.objects.filter(empresa=self.empresa)
            if reseñas.exists():
                promedio = reseñas.aggregate(models.Avg('calificacion'))['calificacion__avg']
                oferta.promedio_calificacion = round(promedio, 2)
                oferta.save()
            else:
                oferta.promedio_calificacion = 0.0
                oferta.save()