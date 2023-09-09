class Exercicio:
    def __init__(self, treino):
        self.treino = treino

    def get_exercicio(self):
        if self.treino == '1- PEITO | OMBRO | TRÍCEPS':
            return ['PEITO | SUPINO RETO','PEITO | VOADOR'] +['OMBRO | ELEVAÇÃO LATERAL','OMBRO | DESENVOLVIMENTO COM HALTER'] +['TRÍCEPS | TRÍCEPS CORDA','TRÍCEPS | TRÍCEPS MERGULHO']
        elif self.treino == '2- COSTAS | BÍCEPS':
            return ['COSTAS | PUXADA ALTA FRONTAL COM PEGADA ABERTA','COSTAS | REMADA BAIXA','COSTAS | PULL DOWN'] + ['BÍCEPS | ROSCA DIRETA','BÍCEPS | ROSCA MARTELO']
        elif self.treino == '3- PERNA':
            return ['PERNA | AGACHAMENTO','PERNA | EXTENSORA','PERNA | FLEXORA','PERNA | PANTURRILHA SENTADO','PERNA | LEVANTAMENTO TERRA SUMO']