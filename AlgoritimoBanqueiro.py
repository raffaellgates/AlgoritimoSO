def atual_alocacao(processo):
    #retonar uma lista com a alocação corrente do processo ex "return processo = [1, 0, 1, 0]"
    pass


def requisito_maximo(processo):
    #retonar uma lista com Recursos existentes fazendo a o calculo c + a = e
    pass


def subtrair_atualAlocação_requisitoMaximo(atual_alocação, requisito_maximo):
    #retornar uma lista do  resultado da subtracao das listas "requisito_maximo - atual_alocação" 
    pass


def eh_possivel_realizar_processo(subt_mp_cp, recursos_livres):
    #retonar true ou false se $1 > $2 comparando a listas
    pass


def atualiza(recursos_livres, atual_alocação):
    #retonar uma lista somando a duas lista
    pass


def remove_elemento_do_conjunto(processo, conjunto_de_processos):
    #remover processo do conjunto
    pass


def algoritmo_do_banqueiro(conjunto_de_processos, recursos_livres):
    while (conjunto_de_processos != []):
        deadlock = False
        for processo in conjunto_de_processos:
            atual_alocação = atual_alocacao(processo)
            requisito_maximo = requisito_maximo(processo)
            subt_mp_cp = subtrair_atualAlocação_requisitoMaximo(atual_alocação, requisito_maximo)
            eh_maior = eh_possivel_realizar_processo(subt_mp_cp, recursos_livres)
            if (eh_maior==True):
                # p pode obter tudo de que necessita.
                # Suponha que ele faz isso, termina, e libera o que ele já tem.
                recursos_livres = atualiza(recursos_livres, atual_alocação)
                conjunto_de_processos = remove_elemento_do_conjunto(processo, conjunto_de_processos)
                deadlock = True

        if (not deadlock):
            print('INSEGURO')
        else:
            print('SEGURO')


def main():
    recursos_disponiveis = [2, 1, 0, 0]
    matriz_requisicoes = [[2, 0, 0, 1], [1, 0, 1, 0], [2, 1, 0, 0]]
    alocacao_corrente = [[0, 0, 1, 0], [2, 0, 0, 1], [0, 1, 2, 0]]
    algoritmo_do_banqueiro(matriz_requisicoes, recursos_disponiveis)


