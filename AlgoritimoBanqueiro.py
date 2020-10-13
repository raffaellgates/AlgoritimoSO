recursos_disponiveis = []
matriz_requisicoes = []
alocacao_corrente = []

def atual_alocacao_processo(processo):
    #retonar uma lista com a alocação corrente do processo ex "return processo = [1, 0, 1, 0]"
    return alocacao_corrente[processo]

def subtrair_atualAlocação_requisitoMaximo(atual_alocacao, requisito_maximo):
    #retornar uma lista do  resultado da subtracao das listas "requisito_maximo - atual_alocação" 
    sub = []
    try:
        for i in range(len(requisito_maximo)):
            valor = requisito_maximo[i] - atual_alocacao[i]
            sub.append(valor)
    except Exception:
        print("quantidade de valores diferentes")
    return sub

def eh_possivel_realizar_processo(subt_mp_cp, recursos_livres):
    #retonar true ou false se $1 > $2 comparando a listas
    is_true = True
    for i in range(len(subt_mp_cp)):
        if(subt_mp_cp[i] > recursos_livres[i]):
            is_true = False
    return is_true

def atualiza(recursos_livres, atual_alocacao):
    #retonar uma lista somando a duas lista
    for i in range(len(recursos_disponiveis)):
        recursos_disponiveis[i] = recursos_livres[i] + atual_alocacao[i] 

def remove_elemento_do_conjunto(processo):
    #remover processo do conjunto
    del(matriz_requisicoes[processo])
    del(alocacao_corrente[processo])

def algoritmo_do_banqueiro(conjunto_de_processos, recursos_livres):
    while (conjunto_de_processos != []):
        deadlock = False
        processo = 0
        for proc in conjunto_de_processos:
            atual_alocacao = atual_alocacao_processo(processo)
            eh_maior = eh_possivel_realizar_processo(proc, recursos_livres)
            if (eh_maior==True):
                atualiza(recursos_livres, atual_alocacao)
                remove_elemento_do_conjunto(processo)
                deadlock = True
                if (processo > 0):
                    processo -= 1
        processo += 1

        if (not deadlock):
            return 'INSEGURO'
    return 'SEGURO'

def main():
    recursos_existentes_matriz = []
    while(True):
        print("Infome o tipo do recurso: ")
        recurso = input("\nnome: ")
        print("Infome a quantidade do recurso: ")
        quantidade = int(input("\nquantidade: "))
        recursos_existentes_matriz.append([recurso, quantidade])
        segue = input("\nDigite '0' se deseja encerrar a escolha de recursos, se não Enter >>> ")
        if (segue == '0'):
            break
    
    print("\n---------Infome a quantidade de recursos disponiveis---------- ")
    quantidade = []
    for d in range(len(recursos_existentes_matriz)):
        print("\nInfome a quantidade de recurso disponivel de {}".format(recursos_existentes_matriz[d][0]))
        quant = int(input("quantidade: "))
        quantidade.append(quant)
    recursos_disponiveis = quantidade

    print("\n---------Infome a quantidade de processo---------- ")
    count_proc = int(input("quantidade: "))
    for i in range(count_proc):
        quantidade = []
        for j in range(len(recursos_existentes_matriz)):
            print("\n---------Infome as requisicoes de recurso do P{}--------- ".format(i+1))
            print("\nInfome a quantidade de recurso de {}".format(recursos_existentes_matriz[j][0]))
            quant = int(input("quantidade: "))
            quantidade.append(quant)
        matriz_requisicoes.append(quantidade)

    for m in range(count_proc):
        quantidade = []
        for n in range(len(recursos_existentes_matriz)):
            print("\n---------Infome a alocacao correte do processo P{}--------- ".format(m+1))
            print("\nInfome a quantidade de recurso de {}".format(recursos_existentes_matriz[n][0]))
            quant = int(input("\nquantidade: "))
            quantidade.append(quant)
        alocacao_corrente.append(quantidade)
    
    resultado = algoritmo_do_banqueiro(matriz_requisicoes, recursos_disponiveis)

    print(resultado)

main()