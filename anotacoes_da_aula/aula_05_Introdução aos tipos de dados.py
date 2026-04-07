
"""
Nessa aula, vamos falar sobre os tipos de dados boleanos. 
Mas o que são? 

São variáveis que guardam dois tipos de informações: verdadeiro ou falso.
Simples assim. Mas usamos o valor true = verdadeiro | false = falso.

Ou é um, ou é outro.

No python, temos vários tipos de operadores lógicos, mas para questionar se um
determinado valor é igual ao outro, vamos usar o " == ".

"""
print("============================================================================");
print("Agora, vamos ver sobre o tipo Boleano.");
print("True", "Verdadeiro", sep=" → ");
print("False", "False", sep=" → ");

print("Note que eles começa com letra maiúscula.");
print("No python, não existe true e false com minúsculo");
print("Se liga nos exemplos:");
print("10 = 10 ?", 10 == 10, sep=" : ");
print("10 = 11 ?", 10 == 11, sep=" : ");
print("Viu que ele retornou True para Sim e False pra Não");

print();
print("Agora, vamos brincar e ver como é a class objeto deles.");
print(type (10 == 10));
print(type(10 == 11));
print("Tanto para verdadeiro ou falso, ela continua sendo class \"bool\"");
print("============================================================================");

print();
