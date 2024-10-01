# Usando uma lista de dicionários para armazenar os dados do desempenho dos residentes

treinamentos = []

def registrar_treinamento(id_residente, id_tutor, cenario, nota):
    treinamento = {
        'id_residente': id_residente,
        'id_tutor': id_tutor,
        'cenario': cenario,
        'nota': nota
    }
    treinamentos.append(treinamento)
    
    print(f"Treinamento registrado para Residente {id_residente} no Cenário '{cenario}' com Nota {nota}.")

# Função para obter o desempenho de um residente específico
def obter_desempenho_residente(id_residente):
    desempenho = [treinamento for treinamento in treinamentos if treinamento['id_residente'] == id_residente]
    if desempenho:
        return desempenho
    else:
        print(f"Residente {id_residente} não possui treinamentos registrados.")
        return []

def calcular_media_residente(id_residente):
    desempenho = obter_desempenho_residente(id_residente)
    
    if not desempenho:
        print(f"Residente {id_residente} não possui treinamentos registrados.")
        return None
    
    soma_notas = sum(treinamento['nota'] for treinamento in desempenho)
    media = soma_notas / len(desempenho)
    return media
    
# Usando classes para organizar o código

class SessaoTreinamento:
    def __init__(self, id_tutor, cenario, nota):
        self.id_tutor = id_tutor
        self.cenario = cenario
        self.nota = nota

class Residente:
    def __init__(self, id_residente):
        self.id_residente = id_residente
        self.treinamentos = []

    def adicionar_treinamento(self, id_tutor, cenario, nota):
        sessao = SessaoTreinamento(id_tutor, cenario, nota)
        self.treinamentos.append(sessao)

    def obter_desempenho(self):
        if self.treinamentos:
            return [(treinamento.cenario, treinamento.nota) for treinamento in self.treinamentos]
        else:
            print(f"Residente {self.id_residente} não possui treinamentos registrados.")
            return []

# Exemplo de uso

registrar_treinamento(1, 101, 'Cenário A', 85)
registrar_treinamento(1, 102, 'Cenário B', 90)
registrar_treinamento(2, 101, 'Cenário A', 88)

print(obter_desempenho_residente(1))
media_residente_1 = calcular_media_residente(1)
print(f"Média de desempenho do Residente 1: {media_residente_1}")

#Exemplo usando classes

residente1 = Residente(1)
residente1.adicionar_treinamento(101, 'Cenário A', 85)
residente1.adicionar_treinamento(102, 'Cenário B', 90)

residente2 = Residente(2)
residente2.adicionar_treinamento(101, 'Cenário A', 88)

desempenho_residente_1 = residente1.obter_desempenho()
print(f"Desempenho do Residente 1: {desempenho_residente_1}")

desempenho_residente_2 = residente2.obter_desempenho()
print(f"Desempenho do Residente 2: {desempenho_residente_2}")