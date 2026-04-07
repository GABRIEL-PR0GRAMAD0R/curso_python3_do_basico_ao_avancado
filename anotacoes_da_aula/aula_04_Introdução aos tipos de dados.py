

# Para comentar várias linhas, vamos usar CONTROL K C.
# Para descomentar várias linhas simultâneamente, vamos usar o CONTROL K U.

"""
Na aula de hoje falamos sobre os tipos de números no Python. 

Números inteiros: 1,2,0,-1,-2 e assim por diante.
Números inteiros não têm casas decimais e por isso não inteiros. 
A eles, damos o tipo primitivo de INT.

Por isso
"""
print();
print("======================================================");
print("Essas são números do tipo primitivo inteiro.");
print(-1);
print(0);
print(1);

"""
Agora, vamos falar dos números flutuantes. 
Estamos falando de números que possuem casas decimais. 
O tipo primitivo deles é float. 

Ele pode representar números negativos e positivos, como nos exemplos anteriores.


Ah, detalhe! 
Sempre use um '.' para indicar as casas decimais. A ',' é usada para concatenação e outras coisas.
"""
print();
print("======================================================");
print("Esses são exemplos de números com pontos flutuantes:")
print(-1.5);
print(0.6);
print(2.0);

"""
Mas como podemos fazer para descobrir o tipo primitivo de uma variável?
Simples, vamos usar a FUNÃO TYPE. 

Essa classe que vamos chamar de "função", vai nos dizer o tipo primitivo de uma variável. 
Fazendo isso, type(objeto que desejamos saber)
ele vai retornar de qual classe é esse objeto. 
Tudo em python é um objeto. 

Vamos a prática!
"""
print();
print("======================================================");
print("Vamos treinar a função TYPE Agora");

print("Para fazer isso, vamos usar a função type()");
print(" Depois, colocamos o objeto dentro do parenteses.")

print();
print("Tipo String: \"Gabriel\" ");
print(type("Gabriel"));

print();
print("Tipo inteiro: \"24 e -24\"");
print (type(24), type(-24));

print();
print("Tipo flutuante \"2.5 e -2.2\"");
print(type(2.5), type(-2.2));
