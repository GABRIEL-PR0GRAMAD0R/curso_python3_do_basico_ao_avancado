"""
Nessa aula vamos falar de precedência entre os operadores aritméticos, ou seja, quem vem antes, quem tem prioridade de resolução.

1º ()
  - Os paranteses sempre virão primeiro. Tudo estiver dentro dos parenteses é resolvido primeiro. 

2º ** 
  - O sinal de elevação é o que vem depois dos parenteses. Se houver primeiro os () e depois **, o que tiver dentro dos parenteses será 
  resolvido primeiro. 

3º * ; / ; // ; %
  - O terceiro lugar de procedencia vai para os operadores de multiplicação "*" e de divisão "/".

4º + ou -
  - O último lugar da nossa lista vai para os sinais de adição e subtração. Então só depois de resolver todos acima, aí o python vai pra
  esse tipo de operação.   


"""

print("Imagine eu quero fazer o seguinte, quero fazer um cálculo.");
print("Quero saber qual o resultado da seguinte operação matemática:");
print("50 + 35 * 2 - 90 / 2 = ?");
print(" Eu quero que o resultado dê 15!");

print();
print("Mas se colcoarmos assim no pythom, olha o que rola: ", end="");
print(50 + 35 * 2 - 90 / 2 );
print();

print("Por que deu esse resultado? Simples, porque o python seguiu uma procedencia de cálculo.");
print("Como expliquei acima, existe uma lista de procedência na matemática e nas linguagens.");
print(""" 
      1º ()
      2º **
      3º * ; / ; // ; %
      4º + ou - 
      """);

print("Se eu quero que dê 15, preciso fazer a correta precedência desse cálculo:");
print("Como eu faria isso? Simples: ");
print("((50 + 35 * 2) - 90 ) / 2 = ",((50 + 35 * 2) - 90 ) / 2);
print();

print("E como isso ocorreu? Simples:");
print("1º - Primeiro ele resolve o que está entre parenteses, o última sempre primeiro.");
print("(50 + 35 * 2 ) → 50 + 70 = 120");
print("");

print("Mas olha ali em cima, a multiplicação tem prioridade:");
print("((120) - 90) → 30 ");
print("30 / 2 → 15 ");
print("");
print("Sacou essa? Fácil, né?");


print("");