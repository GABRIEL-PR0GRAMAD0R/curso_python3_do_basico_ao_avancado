"""
Nessa aula falamos sobre algumas peculiaridades de alguns operadores aritiméticos. 
E quando falamos em peculiaridades, é que dependendo do contexto que o símbolo foir inserido ele terá uma função diferente. 
Dúvida?! Se liga só:

Caraio, eu não sei falar e nem escrever pecularidades, errei umas 15 vez. 
"""

# ------------------------------------------------------------------- #
# Declaração das variáveis que vamos utilizar no programa:

#Concatenamos várias letras.
concatenacao = "G" + "A" + "B" + "R" + "I" + "E" + "L";  
multiplicao_de_string = "| FODÃO, LINDÃO | " * 3
# ------------------------------------------------------------------- #

print("O sinal de \"+\" também pode ser usado como concatenação.");
print("Mas o que é isso? Resumindo a opera, é juntar strings");
print("Imagine que eu tenho várias letras e quero juntar tudo.");
print("G", "A", "B", "R", "I", "E", "L", sep=" - ");
print("");

print("Agora, vamos juntar isso com o sinal de '+'.");
print("G + A + B + R + I + E + L → ", concatenacao);
print("");

print("Agora vamos falar do operador de multiplicação \"*\"");
print("Quando usamos ele com uma STR * um número, ele vai imprimir aquela STR na quantidade do valor do inteiro.");

print("Imagine que eu tô num penhasco e lá faz eco.");
print("E como eu ando com a auto estima baixa, os seres celestiais grita uma vez mas tudo faz eco. Se liga: ");

print("Gabriel, você é:");
print(multiplicao_de_string,);

print("Vamos supor que eu queira fazer uma linha com 4 comandos.");
print("\"=\"*25 → Ele vai repetir o caracter \"=\" 25 vezes. Entendeu?");
print("");
print("=" * 110);
print("");