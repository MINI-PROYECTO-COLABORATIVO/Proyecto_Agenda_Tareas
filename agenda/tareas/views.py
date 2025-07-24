from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Importa vistas genéricas basadas en clases
from django.urls import reverse_lazy  # Importa reverse_lazy para redireccionar después de acciones exitosas
from .models import Tarea  # Importa el modelo Tarea desde models.py

# Vista para listar todas las tareas
class ListaTareas(ListView):
    model = Tarea  # Modelo que se va a listar
    template_name = 'tareas/lista.html'  # Plantilla que se usará para mostrar la lista

# Vista para crear una nueva tarea
class CrearTarea(CreateView):
    model = Tarea  # Modelo que se va a crear
    fields = '__all__'  # Se incluirán todos los campos del modelo en el formulario
    success_url = reverse_lazy('lista_tareas')  # Redirección tras crear con éxito
    template_name = 'tareas/formulario.html'  # Plantilla para el formulario de creación

# Vista para editar una tarea existente
class EditarTarea(UpdateView):
    model = Tarea  # Modelo que se va a editar
    fields = '__all__'  # Se incluyen todos los campos para edición
    success_url = reverse_lazy('lista_tareas')  # Redirección tras editar con éxito
    template_name = 'tareas/formulario.html'  # Reutiliza la misma plantilla que CrearTarea

# Vista para eliminar una tarea
class EliminarTarea(DeleteView):
    model = Tarea  # Modelo que se va a eliminar
    success_url = reverse_lazy('lista_tareas')  # Redirección tras eliminar con éxito
    template_name = 'tareas/confirmar_eliminacion.html'  # Plantilla para confirmar la eliminación

# Vista futura para ver el detalle de una tarea (no implementada aún)
# class DetalleTarea(DetailView):
#     model = Tarea
#     template_name = 'tareas/detalle.html'

# Constante de referencia (no funcional, solo decorativa o para uso futuro)
VISTAS_TAREAS = ['ListaTareas', 'CrearTarea', 'EditarTarea', 'EliminarTarea']

# Create your views here. 
