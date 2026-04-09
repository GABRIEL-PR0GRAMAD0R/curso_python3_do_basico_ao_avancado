"""
Nesse exerício temos que calcular a IMC de uma pessoa.
No caso, eu terei que ser capaz de realizar essa opração matemática e acertar a procedência.

Vamos usar dados fictícios, nada real sobre mim.
Bora lá:

Vimos também sobre as Elipses, que sãoo placeholders. 
Mas o que é isso? Simples, o símbolo "..." indica que o código ainda não foi executado e não da erro.
Isso serve para colcarmos em determinados trechos de código que ainda não foram totalmente programados e que precisam ser preenchidos. 

Mas ela tem outras funções também.
"""

# Declaração das variáveis que vamos utilizar no nosso programa:
nome_completo = "Jão Porqueira";
altura_cliente_em_metros = 1.80;
peso_cliente_em_kg = 95;
imc_do_cliente = peso_cliente_em_kg / (altura_cliente_em_metros ** altura_cliente_em_metros);  # Fórmula do IMC: Peso / (Altura²);


print("Nesse exerício vamos calcular o IMC de uma pessoa com os seguintes dados: ");
print("Nome do sujeito: Jão Porqueira;");
print("Altura = 1.80");
print("Peso em KG = 95;");
print("IMC = ?");
print("");

print("E como é feito o cálculo disso?");
print("PESO * (ALTURA ** ALTURA) ");
print("Seguindo essa lógica: ");
print("");

print("95 / (1.80 ** 1.80) = ", imc_do_cliente);



