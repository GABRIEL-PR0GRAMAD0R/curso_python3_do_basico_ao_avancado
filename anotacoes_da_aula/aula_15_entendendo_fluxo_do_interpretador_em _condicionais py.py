"""
Nessa aula falamos um pouco sobre o fluxo de interpretação sequencial das condicionais.
Vimos como boas práticas de identação ajudam o código a funcionar corretamente.  


Vimos também que a sequência é ordenada. 
Se a primeira condição é verdadeira, as outras não são checadas e o Looping se encerra.
Tipo, se vc tem 4 coisas que deseja verificar e as 4 são verdadeiras, somente a primeira é executado.

"""

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')
print("");

print("=========================================");
print("10 = 10?");
if 10 == 10:
    print('Sim, 10 é igual a 10;');
else: 
    print("Não, não é igual!");

print('Bloco fora do If que não é executado.')
print("=========================================");
