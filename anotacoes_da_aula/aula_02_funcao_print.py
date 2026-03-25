print();print();
print("Nesta aula famos sobre algumas formalidades do comando print().");
print("O Python diferencia letras maiúsculas de minúsculas, cuidado!");
print("Aprendemos a como colocar mais de um argumento nessa função.");
print("Depois, aprendemos como manipular os separadores destes argumentos.");
print("Se liga só: ");
print(); 

print("A sequência abaixo está com um espaço como separador. Vos mudar isso!");
print(12, 34, 53);
print();

print("Aqui, vou usar o símbolo ' > ' como separador, se liga: ");
print(12, 34, 53, sep=' > ');

print("Aqui, vou usar o símbolo ' ; ' como separador, se liga: ");
print(12, 34, 53, sep=' ; ');

print("Gabriel", "lindão,", "excelente programador!", sep=' é um ');

"""
Lembre-se da sintaxe: 
    print("mesagem" , sep=" símbolo separador ");
    tanto faz se você usar aspas simples ('') ou aspas duplas ("") no separador.

    Você pode colocar tanto texto quanto números no print. 
    Para separar esses elementos, use a vírgula (,)
"""
print(); 
print("--------------------------------------------------------------------------------------------");
print();
print("Depois falamos de outro argumento muito bacana, o END.");
print("O END vai no final do print() por padão e é o que faz a quebra de linha automática.");
print();

print("Mas se mexermos nisso, podemos manipular e juntar linhas de baixo com linhas de cima");
print("Olha esse exemplo: ");print();

print("O Gabriel é o melhor", end=" > ");
print("Programador de Python da sua cidade"); print();

print(1, 2, 3, 4, 5, end=" → continuando → ");
print(6, 7, 8, 9, 10); print();


print("Eu também posso jogar um caracter e jogar uma quebra de linha.");
print("Olha só:"); print();

print("!" , "@" , "#" , sep=" | ", end=" → \n");
print(1, 2, 3, sep=" | "); 
print("--------------------------------------------------------------------------------------------");
print();

"""
Falamos também sobre o 'C R L F' que fica no visual studio code.
O professor Otávio Miranda ensinou que se estivermos usando um Windows mais antigo ou sem atualizações
vamos ter que usar o end=\r\n para quebrar linhas. 


Significa carry return line feed.

Ele serve para quebrar linhas automaticamente e evitar que fiquemos escrevendo "\r\n" para pular de uma
linha para uma outra. 


No linux e no MAC, vai ser LF.
"""


