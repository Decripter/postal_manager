from django.db import models


# Create your models here.


class Tipos_postais_base(models.Model):

    id = models.BigAutoField(primary_key=True)
    nome_tipo = models.CharField(max_length=30)
    prazo = models.IntegerField()

    def __str__(self):
        return "Tipo Postal: {}, Prazo: {}".format(self.nome_tipo, self.prazo)


class Tipos_postais_db(models.Model):

    id = models.BigAutoField(primary_key=True)
    classe_obj = models.ForeignKey(Tipos_postais_base, on_delete=models.PROTECT)
    sigla_obj = models.CharField(max_length=2)

    def __str__(self):
        return "Tipo Postal: {}, Sigla: {}".format(
            self.classe_obj.nome_tipo, self.sigla_obj
        )


class Objetos_db(models.Model):

    id = models.BigAutoField(primary_key=True)
    destinatario = models.CharField(max_length=70, verbose_name="Destinatário")
    data_inclusao = models.DateField(auto_now_add=True)
    classe_obj = models.ForeignKey(
        Tipos_postais_base, on_delete=models.PROTECT, verbose_name="Tipo"
    )

    def __str__(self):
        return (
            "Número do Objeto: {}, Destinatário: {}, Data de Inclusão: {} - {}".format(
                self.id,
                self.destinatario,
                self.data_inclusao,
                self.classe_obj.nome_tipo,
            )
        )
