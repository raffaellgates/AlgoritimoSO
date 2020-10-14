def main():
	entradas()


def entradas():
	quantum = int(input("Fatia de tempo de execução: "))
	troca_contexto = int(input("Tempo de troca de contexto: "))
	qntd_processos = int(input("Quantidade de processos a serem executados: "))
	processos = []
	tempo_ingresso = int(input("Deseja trabalhar com tempo de ingresso? (1 - Sim, 2 - Não): "))

	for i in range(qntd_processos):
		processos.append(int(input("Tempo de CPU de {}: ".format("P" + str(i+1)))))

	escalonamentoCircular(processos, quantum, troca_contexto, qntd_processos, tempo_ingresso)


def escalonamentoCircular(processos, quantum, troca_contexto, qntd_p, t_ingresso):
	intervalos = []
	tempos_cpu = []
	p_execucao = 0
	tempo = 0
	finalizados = 0

	if (t_ingresso == 1):
		processos_aux = processos.copy()
		ingressos = []
		ingressos_aux = []

		for i in range(qntd_p):
			valor = input("Tempo de ingresso de {}: ".format("P" + str(i+1)))
			ingressos.append(valor)
			ingressos_aux.append(int(valor))

		proximo = ingressos.index(min(ingressos))
		ingressos_aux.sort()
		for j in range(qntd_p):
			processos[j] = processos_aux[proximo]
			ingressos[proximo] = 'a'
			proximo = ingressos.index(min(ingressos))

		comTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados, ingressos_aux)
	else:
		semTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados)


def comTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados, ingressos):
	while (1):
		if (finalizados != qntd_p):

			if (ingressos[p_execucao] <= tempo):
				print("\nTempo de CPU(ut): ", processos, "Ingresso: ", ingressos)
				if (processos[p_execucao] > quantum):
					processos[p_execucao] -= quantum
					tempo += (quantum + troca_contexto)
					tempos_cpu.append(quantum)
					print("Em execução: ", p_execucao)
				elif ((processos[p_execucao] <= quantum) and (processos[p_execucao] != 0)):
					if (finalizados == qntd_p - 1):
						tempo += processos[p_execucao]
					else:
						tempo += (processos[p_execucao] + troca_contexto)

					tempos_cpu.append(processos[p_execucao])
					processos[p_execucao] = 0
					finalizados += 1
					print("Em execução: ", p_execucao)
				else:
					print("{} já finalizou".format(p_execucao))

				intervalos.append(tempo)

			if (p_execucao == len(processos)-1):
				p_execucao = 0
			else:
				p_execucao += 1
		
		else:
			break

	creditos(tempo)


def semTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados):
	while (1):
		if (finalizados != qntd_p):
			print(p_execucao, end=" ")

			if (processos[p_execucao] > quantum):
				processos[p_execucao] -= quantum
				tempo += (quantum + troca_contexto)
				tempos_cpu.append(quantum)
				#print("Maior  ",quantum, end= "")
			elif ((processos[p_execucao] <= quantum) and (processos[p_execucao] != 0)):
				if (finalizados == qntd_p - 1):
					tempo += processos[p_execucao]
				else:
					tempo += (processos[p_execucao] + troca_contexto)

				#print("Menor/ =,  ",processos[p_execucao], end= "")
				tempos_cpu.append(processos[p_execucao])
				processos[p_execucao] = 0
				finalizados += 1
			#else:
				#print("Acabou", end="")
			intervalos.append(tempo)
			
			print("    ", tempo)

			if (p_execucao == len(processos)-1):
				p_execucao = 0
			else:
				p_execucao += 1
		
		else:
			break

	creditos(tempo)


def creditos(tempo):
	enfeite()
	print("\nTodos os processos foram finalizados. \nTempo total da execução: {}u.t.".format(tempo))
	enfeite()


def enfeite():
	print("\n============================================================")

# def escalonamentoCircular(processos, quantum, troca_contexto, qntd_p):
# 	intervalos = []
# 	tempos_cpu = []
# 	p_execucao = 0
# 	tempo = 0
# 	finalizados = 0
# 	while (1):
# 		if (finalizados != qntd_p):
# 			print(p_execucao, end=" ")

# 			if (processos[p_execucao] > quantum):
# 				processos[p_execucao] -= quantum
# 				tempo += (quantum + troca_contexto)
# 				tempos_cpu.append(quantum)
# 				#print("Maior  ",quantum, end= "")
# 			elif ((processos[p_execucao] <= quantum) and (processos[p_execucao] != 0)):
# 				if (finalizados == qntd_p - 1):
# 					tempo += processos[p_execucao]
# 				else:
# 					tempo += (processos[p_execucao] + troca_contexto)

# 				#print("Menor/ =,  ",processos[p_execucao], end= "")
# 				tempos_cpu.append(processos[p_execucao])
# 				processos[p_execucao] = 0
# 				finalizados += 1
# 			#else:
# 				#print("Acabou", end="")
# 			intervalos.append(tempo)
			
# 			print("    ", tempo)

# 			if (p_execucao == len(processos)-1):
# 				p_execucao = 0
# 			else:
# 				p_execucao += 1
		
# 		else:
# 			break

def gerarGrafico():
	pass


def validaEntradas():
	pass


main()
