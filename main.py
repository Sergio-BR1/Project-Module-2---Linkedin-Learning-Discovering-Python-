from datetime import date

#Função para formatar a mensagem final de cada país
def mensagemPrint(lugar, expectativa):
	print(f"\nSe morasse no {lugar}, você teria em média mais {expectativa} dias de vida, o que dá por volta de {expectativa/365:.0f} anos")

def data_limite(lugar, expectativa, dia, mes, ano, aumentaDia):
		#Chega na data da expectativa de vida da pessoa
		data_limite = date(ano+expectativa, mes, dia)
		faltam = data_limite - date.today()
		mensagemPrint(lugar, int(str(faltam).replace(" days, 0:00:00", ""))+aumentaDia)

#Repete para que o usuário escolha outra data, caso escolhe 29/02 em ano não-bissexto
while (True):
	#Repete caso usuário escolha dia 31 nos meses que terminam em 30 ou escolha dia maior do que 29 em fevereiro
	while (True):
		#Repete caso o dia seja menor do que 1 ou maior do que 31
		while (True):
			dia = int(input("Digite seu dia de nascimento: "))
			if (dia <= 31 and dia >=1):
				break
			print ("Número errado, por favor digite um dia entre 1 e 31\n")

		#Repete caso o dia seja mês do que 1 ou maior do que 12
		while(True):
			mes = int(input("Digite seu mês de nascimento: "))
			if (12>=mes>=1):
				break
			print ("Número errado, por favor digite um dia entre 1 e 12\n")
		if ((mes == 2 and dia > 29)):
			print("Fevereiro não tem dia maior do que 29, por favor escolha dia e mês novamente\n")
			continue

		#Verifica se dia 31 não foi escolhido em mês que não vai até 31
		elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
			#Escolher o mês, para exibir corretamente a mensagem de erro
			meses = ["Janeiro", "Fevereiro", "Março","Abril", "Maio", "Junho", "Julho", "Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
			print(f"{meses[mes-1]} não tem dia 31, por favor escolha outro número\n")
			continue

		break
		
	While (True):
		ano = int(input("Digite seu ano de nascimento: "))
		if ano < 0:
			print("Ano inválido, por favor escolha um número positivo para o ano")
			continue
		break

	#termina o loop se a data escolhida não for 29/02 em ano não-bissexto
	if not(mes == 2 and dia == 29 and ((ano%4 > 0 and ano%400 > 0) or (ano%4 == 0 and ano%100 == 0))):
		break

	print(f"O ano {ano} não é bissexto, portanto fevereiro só vai até dia 28. Por favor, escolha outra data\n")

#a biblioteca não aceita data 29/02 mesmo em anos bissextos, então fiz de forma que aceite a data como 28/02 e compense o dia retirado da data de nascimento
aumentaDia = 0
if dia == 29 and mes == 2:
	dia = 28
	aumentaDia = 1
	
data_limite("África do Sul", 58, dia, mes, ano, aumentaDia)
data_limite("Austrália", 83, dia, mes, ano, aumentaDia)
data_limite("Brasil", 76, dia, mes, ano, aumentaDia)
data_limite("Chile", 81, dia, mes, ano, aumentaDia)
data_limite("Costa Rica", 81, dia, mes, ano, aumentaDia)
data_limite("Estados Unidos", 79, dia, mes, ano, aumentaDia)
data_limite("França", 83, dia, mes, ano, aumentaDia)
data_limite("Grécia", 82, dia, mes, ano, aumentaDia)
data_limite("Japão", 84, dia, mes, ano, aumentaDia)
data_limite("México", 75, dia, mes, ano, aumentaDia)
data_limite("Turquia", 78, dia, mes, ano, aumentaDia)
