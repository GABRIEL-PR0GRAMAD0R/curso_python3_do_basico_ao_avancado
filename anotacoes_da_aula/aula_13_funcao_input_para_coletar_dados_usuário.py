"""
Nesta aula, vamos falar sobre como coletar dados dos usuários através da função INPUT.
Serve para coletar dados dos usuários para podermos trabalhar com informações mais precisamente. 

Exemplo: Como que o sistmea vai guardar os dados sobre um usuário?
Primeiro, ele precisa entrar no sistema: 
Entrada → Processamento → Saída.
Usamos 'None' para declarar uma variável como nula, vazia.

Essa é a regra, sem choro.

Se quisermos pegar o valor da variável e ainda mostrar o nome dela, podemos fazer da seguinte maneira:
print("nome_da_variável="), isso dará o valor da variável.

"""

# Declaração das variáveis que vamos utilizar: 
nome_completo = "";
idade = None ;
idade_de_nascimento = None;

# Início da codificação do programa.
nome_completo = input("Digite seu nome completo: ");
idade = input(f"{nome_completo}, Digite a sua idade: ");
idade_de_nascimento = input(f"{nome_completo}, digite a sua data de nascimento: ");
print();
print();

print(f"Mostrando o nome da variável e o valor dela: {nome_completo=}");
print("Para isso, use o comando:");
print("Use nome_da_variável e um sinal de = junto junto}");

print("");
print("");

print("Nessa vc olha e pensa: 'ótimo! Agora eu consigo fazer cálculos.'");
print("Mas calma lá, gafanhoto. É preciso verificar o que o usário digita porque senão o programa quebra.")

print("");
print("");