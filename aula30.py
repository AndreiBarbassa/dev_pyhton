'''
CONSTANTE = Variáveis que nao vao mudar
Muitas condiçoes no mesmo if (ruim)
        <- contadem de complexidade (ruim)
'''
velocidade = 61 #velocidade atual do carro
local_carro = 101 #local em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 =  100 #local onde o radar 1 está
RADAR_RANGE = 1 #a distância onde o radar pega

#VARIÁVEIS:

velocidade_que_o_carro_passou_no_radar_1 = velocidade > RADAR_1

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and velocidade > RADAR_1

if velocidade_que_o_carro_passou_no_radar_1:
    print('O carro está acima da velocidade do RADAR 1')

if carro_passou_radar_1:
    print('Carro passou no RADAR 1')

if carro_multado_radar_1: #maior ou igual e dps menor ou igual, usado para restringir a faixa de atuação do radar1
    print('O carro foi multado em RADAR 1') #na faixa do km 99 a 101 ele sera multado
