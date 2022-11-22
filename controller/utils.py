import datetime
import os.path

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class Util:

    @staticmethod
    def valida_data(data):
        dt = data.split('/') # converte data string em vetor
        # 10/04/2006
        if len(dt) == 3:
            if 0 < int(dt[0]) <= 31:
                if 0 < int(dt[1]) <= 12:
                    hoje = datetime.date.today()
                    if 1900 < int(dt[2]) <= hoje.year:
                        return True
        return False

    @staticmethod
    def tomm(pts):
        return pts / 0.352777

    @staticmethod
    def gerarRelatorioPdf(dados=[], titulo='Meu Relatório'):
        try:
            cnv = canvas.Canvas(os.path.dirname(__file__)+"\\"
                                + titulo.lower().replace(' ', '') + ".pdf", pagesize= A4)
            cnv.drawString(Util.tomm(85), Util.tomm(290), "IFRO - Campus Ariquemes")
            cnv.drawString(Util.tomm(85), Util.tomm(275), titulo)
            if dados != []:
                col = 10
                lin = 250
                for c in dados[0]:
                    cnv.drawString(Util.tomm(col), Util.tomm(lin), str(c).upper())
                    col += 35
                lin -= 5
                for d in dados:
                    col = 10
                    for v in d:
                        cnv.drawString(Util.tomm(col), Util.tomm(lin), str(d[v]))
                        col += 35

                    lin -= 5

            cnv.save()
            return True
        except Exception as e:
            print(e)
            return False

# Util.gerarRelatorioPdf([{"dado1":'fulano', "dado2":'rua x'}], 'Relatório ADS 2022')

