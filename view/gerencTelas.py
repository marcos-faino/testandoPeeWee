from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager

from telaAluno import ViewAluno
from telaTurma import ViewTurma


class TelaInicial(Screen):
    pass


class CadastroTurma(Screen):
    lbl_id_turma = ObjectProperty(None)
    txi_nome = ObjectProperty(None)
    chk_matutino = ObjectProperty(None)
    chk_vespertino = ObjectProperty(None)
    chk_noturno = ObjectProperty(None)
    chk_integral = ObjectProperty(None)
    bt_cad_atual: ObjectProperty(None)


class ListarTurmas(Screen):
    id_turma = ObjectProperty(None)
    col_id = ObjectProperty(None)
    col_nome = ObjectProperty(None)
    col_turno = ObjectProperty(None)
    grid_lista = ObjectProperty(None)


class CadastroAluno(Screen):
    lbl_id: NumericProperty()
    txi_nome: StringProperty()
    txi_nasc: StringProperty()
    txi_renda: NumericProperty()
    sp_turma: ObjectProperty()


class ListarAlunos(Screen):
    chk_pesq_id: ObjectProperty()
    chk_pesq_nome: ObjectProperty()
    txi_pesq_id: StringProperty()
    txi_pesq_nome: StringProperty()
    gl_pesquisa_id: ObjectProperty()
    gl_pesquisa_nome: ObjectProperty()
    layout_pesq_id: ObjectProperty()
    layout_pesq_nome: ObjectProperty()
    layout_lista_alunos: ObjectProperty()
    pesq = ObjectProperty()


class GerenciaTelas(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tela_turma = ViewTurma(self)
        self._tela_aluno = ViewAluno(self)

    def tela_inicial(self):
        self.current = "TelaInicial"

    def tela_cadastro_turma(self, id=None, botao=None):
        self.current = 'CadastroTurma'
        self._tela_turma.montarTelaAt(id, botao)

    def tela_listar_turmas(self):
        self.current = "ListarTurmas"
        self._tela_turma._limpar_tela_listar()

    def tela_cadastro_aluno(self, id="", botao='None'):
        self.current = "CadastroAluno"
        self._tela_aluno.montar_tela_at(id, botao)

    def tela_listar_alunos(self):
        self._tela_aluno.alternar_pesq("id")
        self.current = "ListarAlunos"
        self._tela_aluno._limpar_tela_listar()

    def cadastrar_atualizar(self):
        self._tela_turma.cad_atual_turma()

    def cadastrar_atualizar_aluno(self):
        self._tela_aluno.cad_atual_aluno()

    def buscar_turmas(self):
        self._tela_turma.busca_turmas()

    def buscar_alunos(self):
        self._tela_aluno.busca_alunos()

    def buscar_alunos_nome(self, nome=""):
        self._tela_aluno.busca_alunos(nome)