class Destino:
    def __init__(self, nome, clima, tipo, custo):
        self.nome= nome
        self.clima= clima
        self.tipo=  tipo
        self.custo= custo

    def combina_com(self, clima, tipo, orcamento): 
      return(self.clima == clima and
             self.tipo == tipo and
             self.custo <= orcamento
             )
     
class DestinosLista:
    destinos= [
        Destino("Rio de Janeiro", "quente", "cidade", 2000),
        Destino("Gramado", "frio", "cidade", 2500),
        Destino("Lençóis Maranhenses", "quente", "natureza", 1800),
        Destino("Campos do Jordão", "frio", "natureza", 2300)
    ]