"""ProyectFinalEPDT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name

from django.contrib import admin
from django.urls import path,include

from django.contrib.auth.views import LoginView, logout_then_login
from AppProyectoF.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',pagPrincipal, name = 'pagPrincipal'),

	path('accounts/login/',LoginView.as_view(template_name='login.html') ,name='login'),
    path('logout/',logout_then_login,name='logout'),


    path('carrito/',carrito_view,name='carrito'),

    path('pagar/',pagar_view,name='pagar'),

    path('contactos/',pagContactos,name='contactos'),
    path('pago/',pagPagos, name = 'pagVerificar'),
    path('servicios/',pagServicios, name = 'pagServicios'),
    
    path('registrarProducto/',registrarProducto, name = 'registrarProducto'),
    path('modificar_Producto/<id>/',modificarProducto, name = 'modificarProducto'),
    path('listado_Productos/',listadoProductos, name = 'listadoProductos'),
    path('eliminar_Producto/<id>/',eliminarProducto, name = 'eliminarProducto'),
    
    path('registrar/', registrar, name='registrar'),

    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('sumar/<int:producto_id>/', sumar_producto, name="Sum"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),




    
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
