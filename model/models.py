import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase


class BaseModel(peewee.Model):

    class Meta:
        database = MySQLConnectorDatabase('escolapeewee', user='root', password='',
                                           host='localhost', port=3306, charset='utf8mb4')


class Turma(BaseModel):
    nome = peewee.CharField(50, unique=True)
    turno = peewee.CharField(20, default='Matutino', null=True)

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as erro:
            print(str(erro))


class Aluno(BaseModel):
    nome = peewee.CharField(max_length=100)
    dt_nasc = peewee.DateField()
    renda_fam = peewee.DecimalField()
    turma = peewee.ForeignKeyField(Turma, related_name='turma')

    def __init__(self, *args, **kwargs):
        self._criatabela()
        super().__init__(*args, **kwargs)

    def _criatabela(self):
        try:
            self.create_table()
        except peewee.OperationalError as e:
            print("Erro: " + e)