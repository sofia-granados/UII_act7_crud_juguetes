from django.db import models

# Create your models here.
class Juguetes(models.Model):
    nombre = models.CharField(max_length=100, help_text="nombre completo del juguete")
    categoria = models.CharField(max_length=100, help_text="categoria del juguete")
    garantia = models.TextField(blank=True, null=True, help_text="garantia")
    reseña = models.TextField(blank=True, null=True, help_text="pequeña reseña")
    precio = models.CharField(max_length=100, help_text="precio")
    def __str__(self):
        return f"{self.nombre} {self.categoria} {self.garantia} {self.reseña} {self.precio}"