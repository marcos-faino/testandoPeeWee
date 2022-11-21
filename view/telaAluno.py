from functools import partial

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from controller.alunoctrl import AlunoCtrl
from controller.utils import Util


class ViewAluno:

    def __init__(self, gerenc_tela):
        self._gt = gerenc_tela # para gerenciar a tela com facilidade
        self._telacad = self._gt.get_screen("CadastroAluno")
        self._telalistar = self._gt.get_screen("ListarAlunos")

    def cad_atual_aluno(self):
        control = AlunoCtrl()
        try:
            id_aluno = self._telacad.lbl_id.text
            nome_aluno = self._telacad.txi_nome.text
            data_nasc = self._telacad.txi_nasc.text
            renda = self._telacad.txi_renda.text
            turma = self._telacad.sp_turma.text
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluir_aluno(id_aluno)
                self.busca_alunos()
                self._gt.current = "ListarAlunos"
            else:
                result = control.salvar_atualizar_aluno(id=id_aluno,
                                                        nome=nome_aluno,
                                                        dt_nasc=data_nasc,
                                                        renda_fam=renda,
                                                        turma=turma)
            self._popJanela(result)
            self._limpar_tela()
            self._telacad.txi_nome.focus = True
        except Exception as e:
            print(str(e))
            self._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} o aluno!!!")

    def _limpar_tela_listar(self):
        self._telalistar.txi_pesq_id.text = ""
        self._telalistar.txi_pesq_nome.text = ""
        cabecalho = [
            self._telalistar.ids.col_id,
            self._telalistar.ids.col_nome,
            self._telalistar.ids.col_dt_nasc,
            self._telalistar.ids.col_renda,
            self._telalistar.ids.col_turma,
            self._telalistar.ids.lbl_atual,
            self._telalistar.ids.lbl_excluir
        ]
        self._telalistar.layout_lista_alunos.clear_widgets()
        for c in cabecalho:
            self._telalistar.layout_lista_alunos.add_widget(c)

    def busca_alunos(self, nome=""):
        try:
            control = AlunoCtrl()
            id_pesq = self._telalistar.txi_pesq_id.text
            resultado = control.buscar_aluno(id=id_pesq, nome=nome)
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_aluno, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_aluno, res['lblId'].text))
                self._telalistar.layout_lista_alunos.add_widget(res['lblId'])
                self._telalistar.layout_lista_alunos.add_widget(res['lblNome'])
                self._telalistar.layout_lista_alunos.add_widget(res['lblDtNasc'])
                self._telalistar.layout_lista_alunos.add_widget(res['lblRenda'])
                self._telalistar.layout_lista_alunos.add_widget(res['lblTurma'])
                self._telalistar.layout_lista_alunos.add_widget(res['btAtualizar'])
                self._telalistar.layout_lista_alunos.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)

    def montar_tela_at(self, id_aluno="", botao=None):
        control = AlunoCtrl()
        self._montar_spinner()
        alunos = []
        if id_aluno:
            alunos = control.buscar_aluno(id=id_aluno)
        if alunos:
            for a in alunos:
                self._telacad.lbl_id.text = a["lblId"].text
                self._telacad.txi_nome.text = a["lblNome"].text
                self._telacad.txi_nasc.text = a["lblDtNasc"].text
                self._telacad.txi_renda.text = a["lblRenda"].text
                self._telacad.sp_turma.text = a["lblTurma"].text
                self._telacad.bt_cad_atual.text = botao.text

    def _montar_spinner(self):
        lista_valores = self._buscar_turmas_tela()
        self._telacad.sp_turma.values = lista_valores


    def _buscar_turmas_tela(self):
        control = AlunoCtrl()
        turmas = control.buscarTurmas()
        nomesTurmas =[]
        for turma in turmas:
            nomesTurmas.append(turma['nome'])
        return tuple(nomesTurmas)

    def _limpar_tela(self):
        self._telacad.lbl_id.text = ""
        self._telacad.txi_nome.text = ""
        self._telacad.txi_nasc.text = ""
        self._telacad.txi_renda.text = ""
        self._telacad.sp_turma.text = "Selecione..."
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def alternar_pesq(self, tipo):
        if self._telalistar.txi_pesq_id:
            self._telalistar.txi_pesq_id.text = ""
        if self._telalistar.txi_pesq_nome:
            self._telalistar.txi_pesq_nome.text = ""
        pesqNome = self._telalistar.gl_pesquisa_nome
        pesqId = self._telalistar.gl_pesquisa_id
        self._telalistar.pesq.remove_widget(pesqNome)
        self._telalistar.pesq.remove_widget(pesqId)
        if tipo == "id":
            pesqId.active = True
            pesqNome.active = False
            self._telalistar.pesq.add_widget(pesqId, 2)
        elif tipo == "nome":
            pesqNome.active = True
            pesqId.active = False
            self._telalistar.pesq.add_widget(pesqNome,2)
