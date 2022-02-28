# Função Mãe
def main():
    saudações()
    OpçõesMenu()

# Função Saudações
def saudações():
    print ("Olá Seja Bem-Vindo a loja Tinta Premium")
    print ("Prazer! Eu sou Eduardo o seu assistente virtual ^-^")
    print ("Em que posso lhe ajudar ?")
    print ("")

# Menu
def OpçõesMenu():
    print ("Para ver o catalogo. Digite 1.")
    print ("Para consultar a quantia de tinta necessária de tinta. Digite 2. ")
    print ("Fazer uma compra. Digite 3.")
    print ("Para ter nossos contatos. Digite 4.")
    print ("")
    return EscolhaMenu()

# Mecânica do Menu
def EscolhaMenu():
    escolha = int (input(": "))
    if escolha == 1:
        return catalogo_simples()
    if escolha == 2:
        return catalogo_rendimento(), escolha_CDR()
    if escolha == 3:
        catalogo_compra(), escolha_compra()
    if escolha == 4:
        contatos()

# Catalogo Simples
def catalogo_simples():
    print ("1 - Tinta Óleo ")
    print ("2 - Tinta Acrilica")
    print ("3 - Tinta Esmaltada")
    print ("4 - Tinta Automotiva")
    print ("5 - Spray de Tinta")
    print ("")
    x = int (input ("Se deseja voltar ao menu principal. Digite 0: "))
    print ("")
    if x == 0:
        return OpçõesMenu()

# Catalogo de Rendimento
def catalogo_rendimento():
    print ("1 - Tinta Óleo - Galão 3l, rende 5 metros quadrados")
    print ("2 - Tinta Acrilica - Galão 3l, rende 2 metros quadrados")
    print ("3 - Tinta Esmaltada - Galão 3l, rende litros 6 metros quadrado")
    print ("4 - Tinta Automotiva - Galão 3l, rende litros 6.5 metros quadrado")
    print ("5 - Spray de Tinta - 1 lata, rende 2 metros quadrado")
    print ("")

# Mecânica do Calculo de Rendimento
def escolha_CDR():
    tinta = int (input("Que tipo de tinta deseja usar? "))
    if tinta == 1:
        return calculo_de_rendimento_1()
    if tinta == 2:
        return calculo_de_rendimento_2()
    if tinta == 3:
        return calculo_de_rendimento_3()
    if tinta == 4:
        return calculo_de_rendimento_4()
    if tinta == 5:
        return calculo_de_rendimento_5()

# Rendimento Tinta Óleo
def calculo_de_rendimento_1():
    largura = float (input("Qual a largura da parede que deseja pintar? "))
    altura = float (input("Qual a altura da parede que deseja pintar? "))
    area = largura * altura
    rendimento = area / 5
    if rendimento < 1:
        rendimento = 1
    print ("É necessário pelo menos", rendimento, "galões de 3l para pintar a área de", area, "metros quadrados")

# Rendimento Tinta Acrilica
def calculo_de_rendimento_2():
    largura = float (input("Qual a largura da parede que deseja pintar? "))
    altura = float (input("Qual a altura da parede que deseja pintar? "))
    area = largura * altura
    rendimento = area / 2
    if rendimento < 1:
        rendimento = 1
    print ("É necessário pelo menos", rendimento, "galões de para pintar a área de", area, "metros quadrados")

# Rendimento Tinta Esmaltada
def calculo_de_rendimento_3():
    largura = float (input("Qual a largura da parede que deseja pintar? "))
    altura = float (input("Qual a altura da parede que deseja pintar? "))
    area = largura * altura
    rendimento = area / 6
    if rendimento < 1:
        rendimento = 1
    print ("É necessário pelo menos", rendimento, "galões para pintar a área de", area, "metros quadrados")

# Rendimento Tinta Automotiva
def calculo_de_rendimento_4():
    largura = float (input("Qual a largura da parede que deseja pintar? "))
    altura = float (input("Qual a altura da parede que deseja pintar? "))
    area = largura * altura
    rendimento = area / 6.5
    if rendimento < 1:
        rendimento = 1
    print ("É necessário pelo menos", rendimento, "galões para pintar a área de", area, "metros quadrados")

# Rendimento Tinta Spray
def calculo_de_rendimento_5():
    largura = float (input("Qual a largura da parede que deseja pintar? "))
    altura = float (input("Qual a altura da parede que deseja pintar? "))
    area = largura * altura
    rendimento = area / 2
    if rendimento < 1:
        rendimento = 1
    print ("É necessário pelo menos", rendimento, "latas para pintar a área de", area, "metros quadrados")

# Catalogo de Compra
def catalogo_compra():
    print ("1 - Tinta Óleo - Galão 3l, R$ 100,00")
    print ("2 - Tinta Acrilica - Galão 3l, R$ 50,00")
    print ("3 - Tinta Esmaltada - Galão 3l, R$ 150,00")
    print ("4 - Tinta Automotiva - Galão 3l, R$ 230,00")
    print ("5 - Spray de Tinta - 1 lata, R$ 10,00")
    print ("")

# Mecânica de Compra
def escolha_compra():
    print ("Digite o número do produto e a quantidade de unidades desejada")
    print ("Para finalizar a compra. Digite 0")
    print ("")
    produtoescolhido = 1
    quantidade = 1
    lista_compra = []
    comprando = True
    while comprando == True:
        produtoescolhido = int (input ("Qual o código do produto que deseja adquiri ? "))
        if produtoescolhido == 0:
            comprando = False
        if produtoescolhido > 5 or produtoescolhido < 1:
            print ("O código de produto inserido está invalido")
            comprando = False
        produtoescolhido = produtoescolhido - 1
        quantidade = int (input ("Quantas unidades deseja deseja? "))
        produtos = [100, 50, 150, 230, 10]
        lista_compra.append(((produtos[produtoescolhido]) * quantidade))
    final = (sum(lista_compra))
    return print ("O valor de sua compra é: R$", final,"reais.")

# Contatos
def contatos():
    print ("")
    print ("Se deseja falar conosco o senhor(a) pode nos contactar pelos seguintes veiculos:")
    print ("")
    print ("Telefone/Whatsapp: (75) 9.9958-1245")
    print ("E-mail: tintaspremium@gmail.com")
    print ("Instagram: @tintas_premium")

# Inicialização do Programa
main()