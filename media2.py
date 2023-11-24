
print(" Calculo de media")
numero = 1

qnt_alunos = int(input("Digite a quantidade de alunos?\n"))
while numero<=qnt_alunos:
  print("{} de {}".format(numero, qnt_alunos))
  nome = input("Nome do aluno\n")
  nota1 = float(input("Insira a nota 1\n"))
  nota2 = float(input("Insira a nota 2\n"))

  media = (nota1 + nota2)/2

  print("{}, sua média é {}".format(nome, media))

  numero +=1

