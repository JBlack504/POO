#Clase usuario que funcionara como una clase abstracta o superior de la cual heredaran 
#las clases empleado y la clase candidato.

class Usuario:
    
    def __init__(self,nombre,correo,contrasena,tipo):
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipo = tipo
        
    def registrar():
        print('registro exitoso')

    def iniciar_sesion():
        print('iniciando sesion')
        
        
class Empleador(Usuario):
    
    def __init__(self, nombre, correo, contrasena, tipo, nombre_empresa, descripcion_empresa ):
        super().__init__(nombre, correo, contrasena, tipo)
        self.nombre_empresa = nombre_empresa
        self.descripcion_empresa = descripcion_empresa
        
    def publicar_oferta():
        print('vacio')
    
    
    def editar_oferta():
        print('vacio')

class Candidato(Usuario):
    
    def __init__(self, nombre, correo, contrasena, tipo, especialidades, habilidades, experiencia):
        super().__init__(nombre, correo, contrasena, tipo)    
        self.especialidades = especialidades
        self.habilidades = habilidades
        self.experiencia = experiencia
        
        
    def crear_perfil():
        print("vacio")
        
    def editar_perfil():
        print("vacio")
        
class Resena:
    def __init__(self, contenido, calificacion):
        self.contenido = contenido
        self.calificacion = calificacion
        
    def agregar_resena():
        print('vacio')
        
class Oferta_laboral():
    
    def __init__(self, titulo, descripcion, topicos):
        self.titulo = titulo
        self.descripcion = descripcion
        self.topicos = topicos
        
    def crear_oferta():
        print("vacio")
        
    def editar_oferta():
        print("vacio")
