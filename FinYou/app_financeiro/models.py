from django.db import models

# Criando os modelos do meu banco de dados


class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    idade = models.IntegerField(max_length=2)
    email = models.EmailField(max_length=254, blank=False, null=False)
    createcleard_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.name
