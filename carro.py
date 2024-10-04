def tabelafit ():
    print("\n 1- Bateria R$200,00")
    print("\n 2- Pneu R$350,00")
    print("\n 3- Filtro de oleo R$50,00")
    print("\n 4- Pastilha R$100,00")
    print("\n 5- Sair do sistema")

tabelafit ()

quantidade = int(input("informe a quantidade :"))
compra = int(input("informe o codigo do produto :"))

match compra :
    case 1 :
        print ("o valor sera :", quantidade * 200)
    case 2 :
        print ("o valor sera :", quantidade * 350)
    case 3 : 
        print("o valor sera :", quantidade * 50 )
    case 4 :
        print("o valor sera :", quantidade * 100)
    case __ :
        print("opcao invalida")
        tabelafit ()
 