"""
Nessa aula vamos falar brevemente sobre as F Strings.
O que são? São saídas formatadas que facilitam a maneira como apresentamos algo na tela.

E por que isso é útil? Eu nem vou te responder, pq senão, te mando ir tomar aonde o sol não bate.
Vamos lá...

Vamos lá, vou mostrar como fazer essa formatação.
Ao invés de ficar ditando um monte de vírgulas e um monte de + para ficar fazendo concatenação
podemos usar a formatação de saída que facilita tudo. 

Exemplo do exercício anterior:
"""

nome_completo = "Jão Porqueira";
altura_cliente_em_metros = 1.80;
peso_cliente_em_kg = 95;
imc_do_cliente = peso_cliente_em_kg / (altura_cliente_em_metros ** altura_cliente_em_metros);  # Fórmula do IMC: Peso / (Altura²);

Resultado = f"{nome_completo} tem {altura_cliente_em_metros} metros de altura e pesa {peso_cliente_em_kg}KG."
Resultado_2 = f"O cliente {nome_completo} tem o IMC = {imc_do_cliente}."


print("");
print("Nesse exemplos nós estamos calculando o IMC de uma pessoa e vamos aprender uma maneira mais fácil de imprimir isso na tela.");
print("");

print("=" * 60);
print("Dados do cliente:")
print(f"Nome do sujeito:{nome_completo};");
print(f"Altura = {peso_cliente_em_kg}");
print(f"Peso em KG = {peso_cliente_em_kg};");
print("=" * 60);
print("");

print("=" * 60);
print(f"{Resultado}");
print(f"{Resultado_2}");
print("=" * 60);

print("");
print("Mas como eu fiz isso? Eu coloquei um f na frente do print.");
print("");
print("     print( f\" string { NOME_DA_VARIÁVEL } string \").");
print("")
print("=" * 60);
print("")

print("Agora, vamos aprender a formatar essas casas decimais. ");
print("Viu que ficou uma merda? Para corrigir isso, usamos o format.");
print(f"Antes: {imc_do_cliente} ");
print(f"Depois: {imc_do_cliente:.2f} ");
print("");

print("Como eu fiz isso? Simples: ");
print("     f\"{ NOME_DA_VARIÁVEL : .2F}");

print("");
print("Você tem que colocar tudo junto para dar certo. Ignore as \\ \\, é só pra não dar erro.");
print("Por que eu coloquei o '.2f'?");
print("Para dizer para ao Python que ali eu quero apenas 2 casas decimais.");
print("");

print("Podemos fazer isso também nas variáveis, pega a visão: ");
print("Resultado = f{ nome_completo} tem { altura_cliente_em_metros} metros de altura e pesa {peso_cliente_em_kg}KG.");
print("");

print("Repare que eu coloquei uma variável do tipo string, depois dei o valor e coloquei o f antes de passar o atributo.");
print("Exemplo: nome_da_variável = f\"blablabla { nome_da_variável} blablabla\"");
print("");
