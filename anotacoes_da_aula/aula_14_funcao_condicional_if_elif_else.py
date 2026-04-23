"""
Nessa aula vamos falar um pouco sobre as condicionais:

    IF      |        ELIF         |    ELSE
    SE      |      SE NÃO SE      |   SE NÃO   

As condicionais alteram o fluxo de saída e de comportamento de um programa.
 
Não da pra existir um ELIF ou um ELSE sem haver pelo menos um IF.
O IF é a única condicional que pode ficar sozinha, depender das outras.
"""
#Variáveis que vamos utilizar: 
comida_favorita = None  # Cria uma variável com um espaço vázio e não da erro por ela estar vazia.

print("Qual a sua comida favorita? ");
print("A) - Macarrão com vina");
print("B) - Torta de Nutella");
print("C) - Salada de alface com tomate");
print("");

print("Esollha uma Letra: A, B ou C");
comida_favorita = input("Digite aqui: ")
print("");

print("==========================================================");
print("Opção escolhida:")
if comida_favorita == "A" or comida_favorita == "a" :
    print("Você escolheu a opção A - macarrão com vina");
    print("Ótima escolha!");
elif comida_favorita == "B"or comida_favorita == "b" :
    print("Você escolheu a opção B - Torta de Nutella");
    print("Excelente escolha!");
elif comida_favorita == "C" or comida_favorita == "c":
    print("Você escolheu a opção C - Salada de alface com tomate");
    print("A escolha de quem ama a saúde!");
else:
    print("Parece que você é uma anta!");
    print("É pra digitar: A, B ou C e nada mais, burro(a)");
    print("É por causa de você que eu tenho que validar tudo que existe. Anta!");

print("");
print("");
