from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicado = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
