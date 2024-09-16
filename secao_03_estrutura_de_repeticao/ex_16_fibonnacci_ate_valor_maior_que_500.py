"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
 valor seja maior que 500.

    >>> calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500()
    '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610'
"""


def calcular_serie_de_fibonacci_ate_valor_ser_maior_que_500() -> str:
    """Escreva aqui em baixo a sua solução"""
    lista_de_fi = [0, 1]
    fi = 1
    while fi < 500:
            fi = (lista_de_fi[-1] + lista_de_fi[-2])
            lista_de_fi.append(fi)
    return ', '.join(map(str, lista_de_fi))

