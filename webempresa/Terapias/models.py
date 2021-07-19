from django.db import models

# Create your models here.


class Terapias(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre_Paciente")
    lastname = models.CharField(max_length=200, verbose_name="Apellido")
    content = models.TextField(verbose_name="Analisis")
    image = models.ImageField(
        verbose_name="Imagen_Paciente", upload_to="Terapias")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "terapia"
        verbose_name_plural = "terapias"
        ordering = ["-created"]

    def __str__(self):
        return self.name
