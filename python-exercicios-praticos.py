# Enunciado:

# Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. 
#  Esse programa deve calcular e mostrar:
# a) A quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado.
# b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

"""
espetaculo = float(input("Entre com o valor total do espetaculo: "))
convite = float(input("Entre com o valor do convite: "))
custoCobrir = espetaculo/convite
lucro = 1.23 * custoCobrir
print(f"A quantidade que deve ser vendida é de {custoCobrir} convites")
print(f"A quantidade que deve ser vendida é de {lucro} convites para ter o lucro de 23%")
"""

# Enunciado:
# Escreva um programa que receba três números quaisquer e apresente:
# a) a soma dos quadrados dos três números;
# b) o quadrado da soma dos três números.

#obs: A função split separa a string nos espaços em branco, gerando uma lista de substrings. Note que os valores são strings após o uso do split.
""" 
n1, n2, n3 = map(float, input("Digite os 3 números separados por espaço: ").split())
somaQuadrados = n1 ** 2 + n2 ** 2 + n3 ** 2
quadradoSoma = (n1+n2+n3) ** 2
print(f"\nA soma dos quadrados dos três números é: {somaQuadrados} e o quadrado da soma dos três números é: {quadradoSoma}")
"""

# Enunciado
# Calcule e apresente o volume de uma lata de óleo (cilindro).
# obs: Se você tem os valores específicos do raio e altura da lata de óleo e deseja calcular o volume usando o valor aproximado de π=3.14 (valor aprox de PI)
""" 
raio, altura = map(float, input("Digite o Raio e depois a altura separado por espaço: ").split())
volume = 3.14 * raio * altura
print(f"O volume da lata de óleo é de {volume:.2f} u.v")
"""

# Enunciado

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Quais sãos as variáveis que preciso? 1º areaPintada > 2º coberturaTinta > 3º tintaVendida > 4º PrecoTotal

areaPintada = float(input("Digite a área do terreno: "))
coberturaTinta = areaPintada / 3
tintaVendida = coberturaTinta / 18
precoTotal = tintaVendida * 80
print(f"A area a ser pintada é {areaPintada}" e deve ser comprado {tintaVendida})




#Parei nesge video: https://www.youtube.com/watch?v=uVJL7tH4SB8&list=PLguMCfF8cJ-G_a5eGd75zBMrkDXTKGRuL&index=3

