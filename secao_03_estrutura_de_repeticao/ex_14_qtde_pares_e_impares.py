"""
Exercício 14 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

    >>> calcular_qtde_numeros_pares_e_impares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    'Existem 5 números pares e 5 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(12, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    'Existem 6 números pares e 4 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(1, 1, 1, 1, 1, 1, 1, 1, 1,1)
    'Existem 0 números pares e 10 números impares'
    >>> calcular_qtde_numeros_pares_e_impares(2, 2, 2, 2, 2, 2, 2, 2, 2,2)
    'Existem 10 números pares e 0 números impares'

"""


def calcular_qtde_numeros_pares_e_impares(n1: int, n2: int, n3: int, n4: int, n5: int, n6: int, n7: int, n8: int, n9: int, n10: int) -> str:
    """Escreva aqui em baixo a sua solução"""

    lista_positiva = []
    lista_negativa= []
    if n1 % 2 == 0:
        lista_positiva.append(n1)
    else:
        lista_negativa.append(n1)
    if n2 % 2 == 0:
        lista_positiva.append(n2)
    else:
        lista_negativa.append(n2)
    if n3 % 2 == 0:
        lista_positiva.append(n3)
    else:
        lista_negativa.append(n3)
    if n4 % 2 == 0:
        lista_positiva.append(n4)
    else:
        lista_negativa.append(n4)
    if n5 % 2 == 0:
        lista_positiva.append(n5)
    else:
        lista_negativa.append(n5)
    if n6 % 2 == 0:
        lista_positiva.append(n6)
    else:
        lista_negativa.append(n6)
    if n7 % 2 == 0:
        lista_positiva.append(n7)
    else:
        lista_negativa.append(n7)
    if n8 % 2 == 0:
        lista_positiva.append(n8)
    else:
        lista_negativa.append(n8)
    if n9 % 2 == 0:
        lista_positiva.append(n9)
    else:
        lista_negativa.append(n9)
    if n10 % 2 == 0:
        lista_positiva.append(n10)
    else:
        lista_negativa.append(n10)

    return f'Existem {len(lista_positiva)} números pares e {len(lista_negativa)} números impares'