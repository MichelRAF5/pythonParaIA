from Monitor import MonitorTemperatura

mt= MonitorTemperatura()

for i in range (5):
    leitura= float(input(f"Digite a {i+1}ª leitura de temperatura: "))
    mt.adicionar_leitura(leitura)

print(mt.intervalo_seguro())

print("Estatísticas das leituras:\n", mt.estatisticas())