from django.db import models  # Importa el módulo de modelos de Django

# Modelo que representa una Tarea en un sistema de gestión de tareas
class Tarea(models.Model):
    # Opciones de prioridad: 1 para Baja, 2 para Media, 3 para Alta
    PRIORIDAD_CHOICES = [
        (1, 'Baja'),
        (2, 'Media'),
        (3, 'Alta'),
    ]

    # Opciones de estado de la tarea
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    
    # Título de la tarea, campo de texto con un máximo de 100 caracteres
    titulo = models.CharField(max_length=100)
    
    # Campo de prioridad que solo acepta las opciones definidas en PRIORIDAD_CHOICES
    prioridad = models.IntegerField(choices=PRIORIDAD_CHOICES)
    
    # Campo de estado que acepta valores definidos en ESTADO_CHOICES
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    
    # Fecha límite para completar la tarea
    fecha_limite = models.DateField()

    def __str__(self):
        # Este método define cómo se muestra una instancia del modelo
        return self.titulo

    def detalles_tarea(self):
        # Método adicional que retorna un resumen de los detalles de la tarea
        return f"Título: {self.titulo}, Prioridad: {self.prioridad}, Estado: {self.estado}, Fecha Límite: {self.fecha_limite}"
    
# Constante para mostrar que se pueden agregar otros valores
COLOR_ETIQUETAS = ['rojo', 'verde', 'azul']

# Create your models here. 
