import numpy as np

class MonitorTemperatura:
    def __init__(self):
        self.lista_leituras= []

    def adicionar_leitura(self, valor):
        self.lista_leituras.append(valor)

    def estatisticas(self):
        dados= np.array(self.lista_leituras)

        estatisticas= {
            'média': np.mean(dados),
            'minímo': np.min(dados),
            'máximo': np.max(dados),
        }
        return estatisticas
    
    def intervalo_seguro(self):
        for i in range(len(self.lista_leituras)):
            if self.lista_leituras[i]<20 or self.lista_leituras[i]>80:
                print(f"A leitura {i+1} está fora do intervalo seguro!")