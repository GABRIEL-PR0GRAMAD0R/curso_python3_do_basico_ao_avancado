"""
As variáveis servem para guardar algo na memória principal do computador.
Como seu nome diz, ela varia a informação guardada. 
Nessa aula nós vamos falar um pouco sobre isso e como atribuir valores.

Vimos também sobre boas práticas em como nomear as variáveis. 
Recomendação: Ler o livro código limpo.

"""
#Declaração de variáveis que vamos utilizar: 
nome_de_usuario = "Gabriel_o_programador_de_python"; #Variável STR
idade_do_usuario = 24; #Variável INT
maior_de_idade = idade_do_usuario >= 18; #Variável BOOL 

print("");
print("Ao invés de ficar repetindo código, usamos as variváies para fazer isso por nós.");
print("Elas guardam os valores úteis para nós para que possamos replicá-las facilmente depois.");
print("");
print("Nome de usuário: ", nome_de_usuario);
print("Idade de usuário: ", idade_do_usuario);

print("O", nome_de_usuario, "é maior de idade:", maior_de_idade);
print("");