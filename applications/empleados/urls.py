from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
        ),
    path(
        'listar-todo-empleados/', 
        views.ListAllEmpleados.as_view(),
        name="empleados-all"
        ), 
    path(
        'listar-by-area-empleados/<shorname>/', 
        views.ListByAreaEmpleados.as_view(),
        name="empleados-by-area-empleados"
        ), 
    path(
        'buscar_empleado/', 
        views.ListEmpeladosByKword.as_view()
        ), 
    path(
        'listar_habilidades_empleado/', 
        views.ListHabilidadesEmpledos.as_view())
    , 
    path(
        'ver_empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name="detalle_empleado"), 
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='add_empleado'), 
    path(
        'success/', 
        views.SuccessView.as_view(),
        name='correcto'
    ), 
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
        ), 
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
        ), 
    path(
        'listar_admin',
        views.ListaEmpleadosAdminsView.as_view(),
        name='lista_admin_empleados'
    )
    
]
