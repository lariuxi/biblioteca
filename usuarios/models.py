from django.db import models


#user: wellington
#senha: Well2020@
#email: wellingtonlariuxi@gmail.com



class Usuario(models.Model):
    nome= models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    ativo = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nome