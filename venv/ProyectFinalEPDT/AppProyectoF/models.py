from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default="Sin Descripcion")
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="imagenesProductos/", null= True,blank = True,default='imagenesProductos/img_no_disponible.png')

    def __str__(self):
        return self.nombre