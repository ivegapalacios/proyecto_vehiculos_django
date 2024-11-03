from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    class Meta:
        permissions = [
            ("visualizar_catalogo", "add_vehiculo_model")
        ]

    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def get_condicion_precio(self):
        if self.precio < 10000:
            return "Bajo"
        elif 10000 <= self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"

    def __str__(self):
        return f"{self.marca} - {self.modelo}"