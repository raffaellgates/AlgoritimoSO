def main():
	entradas()


def entradas():
	enfeite("================")
	enfeite("ENTRADA DE DADOS")
	quantum = int(input("\nFatia de tempo de execução: "))
	troca_contexto = int(input("\nTempo de troca de contexto: "))
	qntd_processos = int(input("\nQuantidade de processos a serem executados: "))
	processos = []

	for i in range(qntd_processos):
		processos.append(int(input("Tempo de CPU de {}: ".format("P" + str(i+1)))))
	tempo_ingresso = int(input("\nDeseja trabalhar com tempo de ingresso? (1 - Sim, 2 - Não): "))

	escalonamentoCircular(processos, quantum, troca_contexto, qntd_processos, tempo_ingresso)


def escalonamentoCircular(processos, quantum, troca_contexto, qntd_p, t_ingresso):
	intervalos = []
	tempos_cpu = []
	turnaround = []
	media = []
	p_execucao = 0
	tempo = 0
	finalizados = 0

	if (t_ingresso == 1):
		processos_aux = processos.copy()
		ingressos = []
		ingressos_aux = []

		for i in range(qntd_p):
			valor = input("\nTempo de ingresso de {}: ".format("P" + str(i+1)))
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


def semTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados):
	enfeite("TIMELINE DE EXECUÇÃO")
	
	print("Valor do QUANTUM: {}u.t.\n".format(quantum))

	while (1):
		print("Tempos de CPU restantes: ", processos)

		if (finalizados != qntd_p):

			print("\nProcesso P{}".format(p_execucao+1))

			if (processos[p_execucao] != 0):
				print("Status: Em execução")
				print("Começo da execução: {}u.t.".format(tempo))

				if (processos[p_execucao] > quantum):
					processos[p_execucao] -= quantum
					tempo += (quantum + troca_contexto)
					tempos_cpu.append(quantum)
				elif ((processos[p_execucao] <= quantum)):
					if (finalizados == qntd_p - 1):
						tempo += processos[p_execucao]
					else:
						tempo += (processos[p_execucao] + troca_contexto)

					tempos_cpu.append(processos[p_execucao])
					processos[p_execucao] = 0
					finalizados += 1
				else:
					print("{} já finalizou".format(p_execucao))

				intervalos.append(tempo)

				if (finalizados == qntd_p):
					print("Término da execução: {}u.t.\n".format(tempo))
				else:
					print("Término da execução: {}u.t.".format(tempo-troca_contexto))
					print("Troca de contexto: {}u.t.\n".format(troca_contexto))
			
			else:
				print("Status: Finalizado\n")

			if (p_execucao == len(processos)-1):
				p_execucao = 0
			else:
				p_execucao += 1
		
		else:
			break

	creditos(tempo)


def comTempoDeIngresso(processos, quantum, troca_contexto, qntd_p, intervalos, tempos_cpu, p_execucao, tempo, finalizados, ingressos):
	enfeite("TIMELINE DE EXECUÇÃO")
	
	print("Valor do QUANTUM: {}u.t.\n".format(quantum))

	while (1):
		print("Tempos de CPU restantes: ", processos, "Ingresso: ", ingressos)

		if (finalizados != qntd_p):

			if (ingressos[p_execucao] <= tempo):

				print("\nProcesso ingresso no tempo {}".format(p_execucao+1))

				if (processos[p_execucao] != 0):
					print("Status: Em execução")
					print("Começo da execução: {}u.t.".format(tempo))

					if (processos[p_execucao] > quantum):
						processos[p_execucao] -= quantum
						tempo += (quantum + troca_contexto)
						tempos_cpu.append(quantum)
					elif ((processos[p_execucao] <= quantum)):
						if (finalizados == qntd_p - 1):
							tempo += processos[p_execucao]
						else:
							tempo += (processos[p_execucao] + troca_contexto)

						tempos_cpu.append(processos[p_execucao])
						processos[p_execucao] = 0
						finalizados += 1

					intervalos.append(tempo)

					if (finalizados == qntd_p):
						print("Término da execução: {}u.t.\n".format(tempo))
					else:
						print("Término da execução: {}u.t.".format(tempo-troca_contexto))
						print("Troca de contexto: {}u.t.\n".format(troca_contexto))
				
				else:
					print("Status: Finalizado\n")


			if (p_execucao == len(processos)-1):
				p_execucao = 0
			else:
				p_execucao += 1
		
		else:
			break

	creditos(tempo)


def creditos(tempo):
	enfeite("FIM DA TIMELINE")
	print("\nTodos os processos foram finalizados com sucesso :) \nTempo total da execução: {}u.t.".format(tempo))
	enfeite("================")


def enfeite(palavra):
	print("\n============================",palavra,"================================\n")


main()
