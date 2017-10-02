from django.db import models

# Create your models here.
class Palestra(models.Model):
    titulo = models.CharField(max_length=300, help_text="Digite o nome da palestra")
    horario = models.ForeignKey('Horario', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.titulo

class Dia(models.Model):
    dia = models.DateField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '%s (%s)' % (self.dia,self.mes)

class Horario(models.Model):
    hora = models.DateTimeField()

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.hora
