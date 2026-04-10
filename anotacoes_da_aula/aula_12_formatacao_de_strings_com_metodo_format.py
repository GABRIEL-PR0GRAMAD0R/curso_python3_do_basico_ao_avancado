"""
Nessa aula vamos falar brevemente sobre a função format. 
Ela é uma maneira alternativa de formatarmos a saída de informações.

Todo objeto tem um método. Ele pode fazer várias ações que são chamadas de objeitos.
Vimos ua breve introdução de como formatar diretamente com o método format e como usar os índices.

Também falamos de parâmetro nomeado, que é quando damos nome a um parâmetro.
Depois de dar nome a um parâmetro, todos os seguintes precisam ser nomeados também, senão, da erro.

Fiz um exemplo.
"""

# Declaração das variáveis que vamos utilizar no nosso programa:
nome = "Gabriel";
idade = 24;
altura = 1.8;
pais_onde_mora = "Brasil";

print("Vamos imprimir algumas coisas com o método .fortmat");
print("""
      Nome: {:*^15}
      Idade: {:*>10}
      Altura: {:*<10,.2f}
      Pais_onde_mora {pais}
      """.format(nome, idade, altura, pais=pais_onde_mora));

print("Acima estão os dados fictícios sobre mim. Eles estão formados na seguinte sintaxe:");
print("Eles estão formados na seguinte sintaxe:");
print("");

print("""print(\"
      Nome: { :*^15} → Vai centralizar e encaixar a string em 15 espaços e se sobrar casinhas, completa com '*'.
        Ele colocou a String e distribuiu espaço restante (8) entre os caracteres '*' .

      Idade: { :*>10} → Vai encaixar jogar símbolos de * a esquerda da string pra daí jogar o valor da strings. 
        Ele colocou 8 porque os outros 2 espaços estão sendo ocupados pelo valor da variável. 
      
      Altura: { :*<10,.2f} → Vai jogar 10 símbolos de * a direita da string pra daí jogar o valor da strings.
         Ele colocou 7 '*' a direita porque os outros 3 espaços estão sendo ocupados pelo valor da variável. 
      
      Pais_onde_mora {pais} \"
      Depois disso, fechamos as aspas e colocamos o .format(argumento 1, argumento 2, ... ... ...)
      .format(nome, idade, altura, pais=pais_onde_mora))""");
print("");

print("");