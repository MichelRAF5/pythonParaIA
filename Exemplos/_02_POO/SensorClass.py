class Sensor:

    def __init__(self, localizacao, min_temp, max_temp): # Método construtor. O nome __init__ vem de "initialize", ou seja, inicializar. Ele serve para configurar os atributos iniciais do objeto.
        # Atributos do sensor:
        self.localizacao= localizacao
        self.min_temp= min_temp
        self.max_temp= max_temp
        self.opeacional= True
        
    def calibrar(self):
        # É um método que atualiza qual sensor está  sendo calibrado.
        print(f"Sensor em {self.localizacao} calibrado")

    def desligar(self):
        operacional=  False
        print(f"Sensor em {self.localizacao} desligado")