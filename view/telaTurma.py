from functools import partial

from kivy.uix.label import Label
from kivy.uix.popup import Popup

from controller.turmactrl import TurmaCtrl


class ViewTurma:

    def __init__(self, gerenc_tela):
        self._gt = gerenc_tela # para gerenciar a tela com facilidade
        self._telacad = self._gt.get_screen("CadastroTurma")
        self._telalistar = self._gt.get_screen("ListarTurmas")

    def cad_atual_turma(self):
        result = ""
        try:
            id_turma = self._telacad.lbl_id_turma.text
            nome = self._telacad.txi_nome.text
            turno = self._ver_turno()
            control = TurmaCtrl()
            if self._telacad.bt_cad_atual.text == "Excluir":
                result = control.excluir_turma(id_turma)
                self.busca_turmas()
                self._gt.current = "ListarTurmas"
            else:
                result = control.salvar_atualizar_turma(nome=nome, turno=turno, id=id_turma)
            self._popJanela(result)
            self._limparTela()
        except Exception as e:
            print(e)
            self._telacad._popJanela(f"Não foi possível {self._telacad.bt_cad_atual.text} a turma!!!")

    def montarTelaAt(self, idturma=None, botao=None):
        control = TurmaCtrl()
        turma = None
        if idturma:
            turma = control.buscar_por_id(idturma)
        if turma:
            for t in turma:
                self._telacad.lbl_id_turma.text = t['lblId'].text
                self._telacad.txi_nome.text = t['lblNome'].text
                self._marcar_turno(t['lblTurno'].text)
                self._telacad.bt_cad_atual.text = botao.text

    def _limparTela(self):
        self._telacad.lbl_id_turma.text = ""
        self._telacad.txi_nome.text = ""
        self._telacad.chk_matutino.active = False
        self._telacad.chk_vespertino.active = False
        self._telacad.chk_noturno.active = False
        self._telacad.chk_integral.active = False
        self._telacad.bt_cad_atual.text = "Cadastrar"

    def _popJanela(self, texto=""):
        popup = Popup(title='Informação', content=Label(text=texto), auto_dismiss=True)
        popup.size_hint = (0.98, 0.4)
        popup.open()

    def _ver_turno(self):
        turno = ""
        if self._telacad.chk_matutino.active:
            turno = self._telacad.chk_matutino.value
        elif self._telacad.chk_vespertino.active:
            turno = self._telacad.chk_vespertino.value
        elif self._telacad.chk_noturno.active:
            turno = self._telacad.chk_noturno.value
        elif self._telacad.chk_integral.active:
            turno = self._telacad.chk_integral.value
        return turno

    def _marcar_turno(self, texto):
        if self._telacad.chk_matutino.value == texto:
            self._telacad.chk_matutino.active = True
        elif self._telacad.chk_vespertino.value == texto:
            self._telacad.chk_vespertino.active = True
        elif self._telacad.chk_noturno.value == texto:
            self._telacad.chk_noturno.active = True
        elif self._telacad.chk_integral.value == texto:
            self._telacad.chk_integral.active = True

    def _limpar_tela_listar(self):
        self._telalistar.id_turma.text = ""
        cabecalho = [
            self._telalistar.col_id,
            self._telalistar.col_nome,
            self._telalistar.col_turno,
            self._telalistar.lbl_atualizar,
            self._telalistar.lbl_excluir
        ]
        self._telalistar.grid_lista.clear_widgets()
        for c in cabecalho:
            self._telalistar.grid_lista.add_widget(c)

    def busca_turmas(self):
        try:
            control = TurmaCtrl()
            idPesq = self._telalistar.id_turma.text
            if idPesq:
                resultado = control.buscar_por_id(idPesq)
            else:
                resultado = control.buscar_todas()
            self._limpar_tela_listar()
            for res in resultado:
                res['btAtualizar'].bind(on_release=partial(self._gt.tela_cadastro_turma, res['lblId'].text))
                res['btExcluir'].bind(on_release=partial(self._gt.tela_cadastro_turma, res['lblId'].text))
                self._telalistar.grid_lista.add_widget(res['lblId'])
                self._telalistar.grid_lista.add_widget(res['lblNome'])
                self._telalistar.grid_lista.add_widget(res['lblTurno'])
                self._telalistar.grid_lista.add_widget(res['btAtualizar'])
                self._telalistar.grid_lista.add_widget(res['btExcluir'])
        except Exception as e:
            print(e)
