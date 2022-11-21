from controller.turmactrl import TurmaCtrl
from models import *

#Salvar aluno
#turma = Turma.get(nome='3ºA')

#aluno = Aluno(nome='Fulano de Tal', dt_nasc='2010-02-12', renda_fam= 5200.00, turma=turma)
#print(aluno.save())

# Salvar
#turma = Turma(nome="3ºD",turno="Vespertino")
#print(turma.save())

# Atualizar
# turma = Turma.get(id=7)
# turma.nome = "3º Atualizado"
# print(turma.save())

# Excluir
# Perigo: se os argumentos estiverem incorretos retornará o primeiro registro
#turma = Turma.get(nome="3ºA")
#print(turma.nome)
# print(turma.delete_instance())

# Buscar todos
#turmas = Turma.select()
#print(type(turmas))
# print([t.nome for t in turmas])

#turmas = Turma.select().where(Turma.nome % ('3º%'))
#print(turmas)
#print([t.nome for t in turmas])

# ctrl = TurmaCtrl()
# turmas = ctrl.buscarTodas()


# for t in turmas:
#    print(t["nome"])




# Buscar um registro específico
# por id:
# print(Turma.get(id=4).nome)
# print(Turma.get_by_id(3).nome)
# print(Turma[2].nome)
# por nome:
# print(Turma.get(nome='3º A').id)
# print(Turma.get(Turma.nome == '3º F').id)
