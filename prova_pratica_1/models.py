from django.db import models

class Studenti(models.Model):
    nome = models.CharField(max_length=20)
    cognome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome + " " + self.cognome

class Verifica(models.Model):
    materia = models.CharField(max_length=20)
    voto = models.IntegerField()
    studente = models.ForeignKey(Studenti, on_delete=models.CASCADE) 

    def __str__(self):
        return self.materia + ": " + str(self.voto)