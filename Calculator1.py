import math
tipoCalculo = int(input("Que tipo de cálculo você quer fazer? "
                        "\n|Básico: 1|"
                        "\n|Bhaskara: 2|"
                        "\n|MMC e MDC: 3|"
                        "\n|Produtos Notáveis: 4|"
                        "\n|Regra de três: 5|"
                        "\n|Porcentagem: 6|"
                        "\n|Juros: 7|"
                        "\n|Média Aritmética: 8|"
                        "\n|Logaritmo: 9|"
                        "\n|Sistemas Lineares: 10|"
                        "\n|Fatoração: 11|"
                        "\n|Pitágoras: 12|"
                        "\n|Seno, Cosseno e Tangente: 13|"
                        "\n|Areas: 14| :"))

if tipoCalculo == 1:
    print("---CÁLCULOS BÁSICOS---")
    tipoOperacao = str(input("Digite que operação você quer: \n(soma, subtração, multiplicação, divisão, potenciação "
                             "ou radiciação): "))
    if tipoOperacao == 'soma':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x + y
        print("A soma entre {} e {} é igual a {}.".format(x, y, s))
    if tipoOperacao == 'subtração':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x - y
        print("A subtração entre {} e {} é igual a {}.".format(x, y, s))
    if tipoOperacao == 'multiplicação':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x * y
        print("A multiplicação entre {} e {} é igual a {}.".format(x, y, s))
    if tipoOperacao == 'divisão':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x / y
        print("A divisão entre {} e {} é igual a {}.".format(x, y, s))
    if tipoOperacao == 'potenciação':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x ** y
        print("A potência entre {} e {} é igual a {}.".format(x, y, s))
    if tipoOperacao == 'radiciação':
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        s = x ** (1/y)
        print("A radiciação entre {} e {} é igual a {}.".format(x, y, s))

if tipoCalculo == 2:
    print("---BHASKARA---")

    a = int(input("Digite a: "))
    b = int(input("Digite b: "))
    c = int(input("Digite c: "))

    x = (b ** 2) - (4 * a * c)

    if x < 0:
        print("Raiz negativa nao pode ser extraida.")
        exit()

    else:
        x = math.sqrt(x)
        x1 = (-b + x) / (2 * a)
        x2 = (-b - x) / (2 * a)
    print("O valor de x1 é {} e o do x2 é {}.".format(x1, x2))

if tipoCalculo == 3:
    print("---MMC E MDC---")
    op = str(input("Você quer calcular mmc ou mdc? "))
    if op == 'mmc':
        num1 = int(input("Digite um número inteiro:"))
        num2 = int(input("Digite outro número inteiro:"))

        if num1 > num2:
            maior = num1
        else:
            maior = num2

        for i in range(maior):
            aux = num1 * i
            if (aux % num2) == 0:
                mmc = aux
        print("O MMC de {} e {} é igual a: {}".format(num1, num2, mmc))
    if op == 'mdc':
        num1 = int(input("Digite um número inteiro:"))
        num2 = int(input("Digite outro número inteiro:"))

        mdc = 1
        if num1 > num2:
            m = num1
        else:
            m = num2
        for i in range(1, m):
            if num1 % i == 0 and num2 % i == 0:
                mdc = i
        print("O MDC de {} e {} é igual a: {}".format(num1, num2, mdc))

if tipoCalculo == 4:
    print("---PRODUTOS NOTÁVEIS---")
    o = int(input("Você que produtos positivos(1) negativos(2) ou diferença de quadrados(3): "))

    if o == 1:
        x = float(input("Escreva o valor de X: "))
        y = float(input("Escreva o valor de Y: "))

        pnp = (x + y)**2
        print("O produto notável positivo de {} e {} é igual a {}.".format(x, y, pnp))

    if o == 2:
        x = float(input("Escreva o valor de X: "))
        y = float(input("Escreva o valor de Y: "))

        pnn = (x - y) ** 2
        print("O produto notável negativo de {} e {} é igual a {}.".format(x, y, pnn))

    if o == 3:
        x = float(input("Escreva o valor de X: "))
        y = float(input("Escreva o valor de Y: "))

        dq = (x + y) * (x - y)
        print("A diferença de quadrados de {} e {} é igual a {}.".format(x, y, dq))

if tipoCalculo == 5:
    print("---REGRA DE TRÊS---")
    vi1 = float(input("Digite o primeiro valor inicial: "))
    vf1 = float(input("Digite o primeiro valor final: "))
    vi2 = float(input("Digite o segundo valor inicial: "))

    vf2 = (vi2 * vf1) / vi1
    print("A regra de três: \n{} - {}\n{} - x\nTerá o valor de x igual a {}.".format(vi1, vf1, vi2, vf2))

if tipoCalculo == 6:
    print("---PORCENTAGEM---")
    vt = float(input("Digite o valor total: "))
    vi = float(input("Digite o valor inicial: "))

    porcent = (vi / vt) * 100
    print("A porcentagem de {} em total de {} é igual a {}.".format(vi, vt, porcent))

if tipoCalculo == 7:
    print("---JUROS---")
    s = str(input("Você quer calcular juros composto ou simples? "))
    if s == 'simples':
        C = float(input("Digite o capital inicial: "))
        i = float(input("Digite a porcentagem(sem o %): "))
        t = float(input("Digite o tempo: "))

        j = C * (i/100) * t
        f = j+C
        print("O valor final de {} sob um aumneto de {} durante {} é igual a {}".format(C, i, t, f))
    if s == 'composto':
        C = float(input("Digite o capital inicial: "))
        i = float(input("Digite a porcentagem(sem o %): "))
        t = float(input("Digite o tempo: "))

        M = C * ((1+(i/100)) ** t)
        print("O valor final de {} sob um aumneto de {} durante {} é igual a {}".format(C, i, t, M))

if tipoCalculo == 8:
    print("---MÉDIA---")

    n = int(input("Digite a quantidade de números: "))
    sn = 0
    i = 0
    while i < n:
        s = float(input("Digite um número: "))
        sn += s
        i = i + 1
    M = sn / n
    print("A média dos números digitados é igual a {}".format(M))

if tipoCalculo == 9:
    print("---LOG---")
    b = float(input("Digite a base do log: "))
    x = float(input("Digite um número: "))

    lg = math.log(x, b)
    print("O log de {} na base {} é igual a {}".format(x, b, lg))

if tipoCalculo == 10:
    print("---SISTEMAS LINEARES---")
    A1 = int(input("Digite o valor que acompanha o 1º X: "))
    B1 = int(input("Digite o valor que acompanha o 1º Y: "))
    A2 = int(input("Digite o valor que acompanha o 2º X: "))
    B2 = int(input("Digite o valor que acompanha o 2º Y: "))
    C1 = int(input("Digite o valor que é resultante da 1ª equação: "))
    C2 = int(input("Digite o valor que é resultante da 2ª equação: "))

    import numpy as np

    A = np.array([[A1, B1], [A2, B2]])
    B = np.array([[C1], [C2]])

    A_inversa = np.linalg.inv(A)
    x = np.dot(A_inversa, B)
    x = np.linalg.solve(A, B)

    print("O valor do sistema é igual a {}, em que o número de cima é o x e o de baixo é y.".format(x))

if tipoCalculo == 11:
    n = int(input("Digite o número a ser fatorado: "))
    c = n
    f = 1
    while c > 0:
        f *= c
        c -= 1
    print("A fatoração de {} é igual a {}.".format(n, f))

if tipoCalculo == 12:
    import math

    print("---Pitágoras---")
    CA = int(input("Digite o cateto adjacente: "))
    CO = int(input("Digite o cateto oposto: "))

    H = math.sqrt((CA ** 2) + (CO ** 2))
    print("A hipotenusa é igual a {}".format(H))

if tipoCalculo == 13:
    print("SEN,COS E TAN")
    import math

    ang = float(input("Digite o ângulo que você deseja: "))
    seno = math.sin(math.radians(ang))
    cos = math.cos(math.radians(ang))
    tang = math.tan(math.radians(ang))

    print("O seno, o cosseno e a tangente de {} são, respectivamente {:.2f}, {:.2f} e {:.2f}.".format(ang, seno, cos,
                                                                                                      tang))

if tipoCalculo == 14:
    print("---AREAS---")
    print("\n (1) quadrado")
    print("\n (2) triangulo")
    print("\n (3) trapezio")
    print("\n (4) losango")
    print("\n (5) circulo")

    n = int(input("Escolha um poligono: "))

    if n == 1:
        b = float(input("Tamanho da base:"))
        a = float(input("Tamanho da altura:"))
        area = b * a
        print("Area igual a:", area)

    if n == 2:
        c = float(input("Tamanho da base:"))
        d = float(input("Tamanho da altura:"))
        area = c * d / 2
        print("Area igual a:", area)

    if n == 3:
        e = float(input("Tamanho da base maior:"))
        f = float(input("Tamanho da base menor:"))
        g = float(input("Tamanho da altura:"))
        area = (e + f) * g / 2
        print("Area igual a:", area)

    if n == 4:
        h = float(input("Tamanho da diagonal:"))
        i = float(input("Tamanho da outra diagonal:"))
        area = h * i / 2
        print("Area igual a:", area)
    if n == 5:
        print("(1) Setor")
        print("(2) Circulo")

        c = int(input("Escolha o tipo de conta:"))

        if c == 1:
            t = float(input("Tamanho do raio:"))
            s = float(input("Angulo em graus:"))
            area = s * t * t * 3.14 / 360
            pi = area / 3.14
            print("Area igual a:", area)
            print("Ou a area em Pi e igual a:", pi)
        if c == 2:
            t = float(input("Tamanho do raio:"))
            area = t * t * 3.14
            pi = area / 3.14
            print("Area igual a:", area)
            print("Ou a area em Pi e igual a:", pi)