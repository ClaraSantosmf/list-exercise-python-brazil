"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

    >>> from secao_01_estrutura_sequencial import ex_16_loja_de_tintas_simples
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '50'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 1 lata(s) tinta ao custo de R$ 80.00
    >>> ex_16_loja_de_tintas_simples.input = lambda k: '100'
    >>> ex_16_loja_de_tintas_simples.calcular_latas_e_preco_de_tinta()
    Você deve comprar 2 lata(s) tinta ao custo de R$ 160.00


"""


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_quadrada = float(input("Diga a área a ser pintada em metros quadrados?"))
    preco_da_lata = 80.00
    litros_necessarios = area_quadrada/3
    latas_necessarias = litros_necessarios//18
    if (litros_necessarios % 18) > 0:
        latas_necessarias += 1
    else:
        latas_necessarias += 0
    print(f'Você deve comprar {latas_necessarias:.0f} lata(s) tinta ao custo de R$ {preco_da_lata * latas_necessarias:.2f}')
