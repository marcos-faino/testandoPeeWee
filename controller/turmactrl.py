from kivy.uix.button import Button
from kivy.uix.label import Label

from model.models import Turma


class TurmaCtrl:

    def salvar_atualizar_turma(self, nome, turno, id=None):
        try:
            if id:
                turma = Turma.get_by_id(id)
                turma.nome = nome
                turma.turno = turno
            else:
                turma = Turma(nome=nome, turno=turno)
            turma.save()
            return "Operação realizada com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar!!!"

    def excluir_turma(self, id):
        try:
            Turma.delete_by_id(id)
            return "Turma excluída com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível excluir a turma!!!"

    def buscar_por_id(self, id):
        lista = []
        try:
            turma = Turma.get_by_id(id)
            lista.append(self._montar_turma(turma.id, turma.nome, turma.turno))
            return lista
        except Exception as e:
            return None

    def buscar_por_nome(self, nome):
        lista = []
        try:
            turma = Turma.get(nome=nome)
            lista.append(self._montar_turma(turma.id, turma.nome, turma.turno))
            return lista
        except Exception as e:
            return None

    def buscar_todas(self):
        try:
            ts = Turma.select()
            lista = []
            for t in ts:
                lista.append(self._montar_turma(t.id, t.nome, t.turno))
            return lista
        except Exception as e:
            return None

    def _montar_turma(self, id, nome, turno):
        minhaturma = {
            'lblId': self._criarLabel(id, 0.2),
            'lblNome': self._criarLabel(nome, 0.4),
            'lblTurno': self._criarLabel(turno, 0.2),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return minhaturma

    def _criarLabel(self, texto, tam):
        label = Label()
        label.text = str(texto)
        label.size_hint_y = None
        label.size_hint_x = tam
        label.height = '30dp'
        return label

    def _criarBotao(self, texto):
        botao = Button(text=texto,
                       font_size='10sp',
                       size_hint_y = None,
                       height='30dp',
                       size_hint_x = .1)
        return botao