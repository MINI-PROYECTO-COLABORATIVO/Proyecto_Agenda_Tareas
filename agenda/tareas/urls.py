from django.urls import path  # Importa la función path para definir URLs
from .views import ListaTareas, CrearTarea, EditarTarea, EliminarTarea  # Importa las vistas desde el archivo views.py

# Lista de rutas URL para las vistas del sistema de tareas
urlpatterns = [
    # Ruta raíz que muestra la lista de tareas
    path('', ListaTareas.as_view(), name='lista_tareas'),

    # Ruta para crear una nueva tarea
    path('crear/', CrearTarea.as_view(), name='crear_tarea'),

    # Ruta para editar una tarea específica, identificada por su clave primaria (pk)
    path('editar/<int:pk>/', EditarTarea.as_view(), name='editar_tarea'),

    # Ruta para eliminar una tarea específica, también por clave primaria
    path('eliminar/<int:pk>/', EliminarTarea.as_view(), name='eliminar_tarea'),

    # Ruta de ejemplo comentada para vista de detalles (podría agregarse en el futuro)
    # path('detalle/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
]

# Constante decorativa (no utilizada) para mostrar cómo se pueden definir otras rutas en grupo
GRUPO_TAREAS = 'modulo_tareas_urls'
