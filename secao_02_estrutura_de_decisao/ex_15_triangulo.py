"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;gi
Triângulo Escaleno: três lados diferentes;

    >>> classificar_trinagulo(2, 3, 4)
    'Triângulo Escaleno'
    >>> classificar_trinagulo(2, 2, 3)
    'Triângulo Isósceles'
    >>> classificar_trinagulo(2, 2, 2)
    'Triângulo Equilátero'
    >>> classificar_trinagulo(2, 2, 5)
    'Não é um triângulo'
    >>> classificar_trinagulo(5, 2, 2)
    'Não é um triângulo'
    >>> classificar_trinagulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_trinagulo(lado_a: float, lado_b: float, lado_c: float):
    """Escreva aqui em baixo a sua solução"""
    if (lado_a + lado_b) < lado_c or (lado_a + lado_c) < lado_b or (lado_b + lado_c) < lado_a:
        return 'Não é um triângulo'
    elif (lado_a == lado_b) and (lado_b == lado_c):
        print("'Triângulo Equilátero'")
    elif ((lado_c != lado_b) and (lado_a != lado_b) and (lado_a != lado_c)):
            print("'Triângulo Escaleno'")
    else:
        print("'Triângulo Isósceles'")
