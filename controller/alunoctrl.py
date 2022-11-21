import locale

from kivy.uix.button import Button
from kivy.uix.label import Label
from peewee import ModelSelect

from controller.utils import Util
from model.models import Aluno, Turma


class AlunoCtrl:

    def salvar_atualizar_aluno(self, id=None, nome=None, dt_nasc=None, renda_fam=None, turma=None):
        try:
            t = Turma.get(nome=turma)
            dn = self._dt_nasc_tela_banco(dt_nasc) # "aaaa-mm-dd"
            rf = self._renda_tela_banco(renda_fam) # 9999.99
            if id:
                aluno = Aluno.get_by_id(id)
                aluno.nome = nome
                aluno.dt_nasc = dn
                aluno.renda_fam = rf
                aluno.turma = t
            else:
                aluno = Aluno(nome=nome, dt_nasc=dn, renda_fam=rf, turma=t)
            aluno.save()
            return "Operação realizada com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível salvar ou atualizar!!!"

    def excluir_aluno(self, id):
        try:
            aluno = Aluno.get_by_id(id)
            aluno.delete_instance()
            return "Aluno excluído com sucesso!!!"
        except Exception as e:
            print(e)
            return "Não foi possível excluir o Aluno!!!"

    def _dt_nasc_tela_banco(self, dt_nasc):
        """
        Converte a data no formato "dd/mm/aaaa" para "aaaa-mm-dd"
        :param dt_nasc:  a data de nascimento que vem da tela
        :return: a data de nascimento no formato do sql Date
        """
        if Util.valida_data(dt_nasc):
            d = dt_nasc.split('/') #converte a string em lista
            databanco = f"{d[2]}-{d[1]}-{d[0]}" # monta uma string no fomato "aaaa-mm-dd"
            return databanco

    def _renda_tela_banco(self, renda):
        """
        Converte a renda no formato "9.999,99" para "9999.99"
        :param renda: a renda vindo da tela
        :return: a renda no formato do banco de dados
        """
        try:
            r = renda.replace(".", "") # remove o ponto da renda
            r = r.replace(",", ".") # troca a virgula por ponto
            return float(r)
        except Exception as e:
            print(e)

    def buscar_aluno(self, id=None, nome=None):
        try:
            if id:
                aluno = Aluno.get_by_id(id)
            elif nome:
                aluno = Aluno.select().where(Aluno.nome % f'%{nome}%')
            else:
                aluno = Aluno.select()
        except Exception as e:
            print(e)
            return None
        itens = []
        if type(aluno) is Aluno:
            itens.append(self._montar_aluno(aluno.id, aluno.nome, aluno.dt_nasc, aluno.renda_fam, aluno.turma.nome))
        elif type(aluno) is ModelSelect:
            for a in aluno:
                itens.append(self._montar_aluno(a.id, a.nome, a.dt_nasc, a.renda_fam, a.turma.nome))
        return itens

    def _dt_nasc_banco_tela(self, data):
        """
        Formata a data para a tela no formato "dd/mm/aaaa"
        :param data: a data do banco de dados
        :return: a data para ser mostrada na tela
        """
        data_tela = ""
        if data:
            data_array = str(data).split("-") # converte a data para array
            data_tela = f'{data_array[2]}/{data_array[1]}/{data_array[0]}'
        return data_tela

    def _renda_banco_tela(self, renda):
        """
        Formata a renda no formato "9.999,99"
        :param renda: a renda salva no banco
        :return: a renda a ser mostrada na tela
        """
        locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
        rendatela = str(locale.currency(renda, grouping=True, symbol=None))
        return rendatela

    def _montar_aluno(self, id, nome, dt_nasc, renda,turma):
        nasc = self._dt_nasc_banco_tela(dt_nasc) # 01/01/2000
        ren = self._renda_banco_tela(renda) # 9.999,99
        meualuno = {
            'lblId': self._criarLabel(id, 0.1),
            'lblNome': self._criarLabel(nome, 0.4),
            'lblDtNasc': self._criarLabel(nasc, 0.1),
            'lblRenda': self._criarLabel(ren,0.1),
            'lblTurma': self._criarLabel(turma,0.1),
            'btAtualizar': self._criarBotao("Atualizar"),
            'btExcluir': self._criarBotao("Excluir")
        }
        return meualuno

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

    def buscarTurmas(self):
        turmasbanco = Turma.select()
        turmas = []
        for turma in turmasbanco:
            turmas.append({"id": turma.id, "nome": turma.nome})
        return turmas