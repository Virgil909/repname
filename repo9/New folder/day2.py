'''
def salnet (salbrut):
    return salbrut*45/100


def salnetprog(salbrut):

    if salbrut > 0 and salbrut <= 3000:
        return salbrut * 40 / 100

    elif salbrut > 3000 and salbrut <= 8000:
        return salbrut * 45 / 100

    elif salbrut > 8000 :
        return salbrut * 50 / 100


def modf(salbrut):
    x = salbrut * 45 / 100
    if salbrut > 0 and salbrut <= 3000:
        print("salariul net creste cu: ")
        print((salbrut * 40 / 100)-x)
    elif salbrut > 3000 and salbrut <= 8000:
        print("Salariul ramane neschimbat")

    elif salbrut > 8000:
       print("salariul se micosreaza cu:")
       print((salbrut * 40 / 100) - x)

x=salnet(1000)
print(x)


y=salnetprog(200)
t=salnetprog(4000)
v=salnetprog(9000)
print(y)
print(t)
print(v)

modf(5000)
modf(2000)
modf(9000)

#ex2


def pensie(nrl, pro, sum):
    total = 0
    nrla = 0
    while (nrla != nrl):
        if nrla % 12 == 0:
            total = total + pro / 100 * total

        total = total + sum
        nrla = nrla + 1

    return total



x=pensie(12,3,1000)
print(x)

'''
'''
#ex3


produse ={ "Pâine albă": {"pret": 3.00, "tva_vechi": 9, "tva_nou": 11}
,
"Făină albă": {"pret": 4.50, "tva_vechi": 9, "tva_nou": 11},
"Mălai": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
"Orez": {"pret": 8.00, "tva_vechi": 9, "tva_nou": 11},
"Paste făinoase": {"pret": 6.00, "tva_vechi": 9, "tva_nou": 11},
"Lapte": {"pret": 6.50, "tva_vechi": 9, "tva_nou": 11},
"Brânză telemea": {"pret": 35.00, "tva_vechi": 9, "tva_nou": 11},
"Iaurt": {"pret": 2.50, "tva_vechi": 9, "tva_nou": 11},
"Ouă": {"pret": 9.00, "tva_vechi": 9, "tva_nou": 11},
"Carne de pui": {"pret": 18.00, "tva_vechi": 9, "tva_nou": 11},
"Carne de porc": {"pret": 25.00, "tva_vechi": 9, "tva_nou": 11},
"Salam / Parizer": {"pret": 20.00, "tva_vechi": 9, "tva_nou": 11},
"Pește congelat": {"pret": 22.00, "tva_vechi": 9, "tva_nou": 11},
"Cartofi": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
"Ceapă": {"pret": 3.50, "tva_vechi": 9, "tva_nou": 11},
"Morcovi": {"pret": 4.00, "tva_vechi": 9, "tva_nou": 11},
"Mere": {"pret": 6.00, "tva_vechi": 9, "tva_nou": 11},
"Banane": {"pret": 8.00, "tva_vechi": 9, "tva_nou": 11},
"Ulei floarea-soarelui": {"pret": 14.00, "tva_vechi": 9, "tva_nou": 11},
"Unt": {"pret": 10.00, "tva_vechi": 9, "tva_nou": 11},
"Zahăr": {"pret": 5.00, "tva_vechi": 9, "tva_nou": 11},
"Sare": {"pret": 2.00, "tva_vechi": 9, "tva_nou": 11},
"Cafea": {"pret": 15.00, "tva_vechi": 5, "tva_nou": 11},
"Detergent": {"pret": 20.00, "tva_vechi": 19, "tva_nou": 21},
"Săpun": {"pret": 4.00, "tva_vechi": 19, "tva_nou": 21},
"Hârtie igienică": {"pret": 10.00, "tva_vechi": 19, "tva_nou": 21},
"Bere": {"pret": 5.00, "tva_vechi": 19, "tva_nou": 21},
"Apă plată": {"pret": 3.00, "tva_vechi": 9, "tva_nou": 11},
"Energizant": {"pret": 7.00, "tva_vechi": 19, "tva_nou": 21},
"Țigări": {"pret": 20.00, "tva_vechi": 20, "tva_nou": 41},
}

# pret total vechi, pret vechi fara tva ,pret total nou

def funct():
    total=0
    print("alegeti ce doriti sa faceti: ")
    print("1:pret total brut ")
    print("2:pret total tva nou ")
    print("3:pret total tva vechi ")
    var=input("introduceti nr")
    match var:
        case "1":
            for prod,inform in produse.items():      #in prima var ai cheia (nume aliment aici) si in a doua ai informatia ce se alfa pe fiecare linie
                prt=inform["pret"]*(100/(100+inform["tva_vechi"]))
                total=total+prt
            return total
        case "2":
            for prod, inform in produse.items():  # in prima var ai cheia (nume aliment aici) si in a doua ai informatia ce se alfa pe fiecare linie
                prt = (inform["pret"] * (100 / (100 + inform["tva_vechi"])))*((100+inform["tva_vechi"]/100))

                total = total + prt
            return total
        case "3":
            for prod, inform in produse.items():  # in prima var ai cheia (nume aliment aici) si in a doua ai informatia ce se alfa pe fiecare linie

                total = total + inform["pret"]

            return total
        case _:
            print("Ati introdus o valoare gresita")


valo=funct()
print(valo)
print("val scadere")

#text=input("introduceti nr")

'''


"""
#ex4
#aceasta functie face:
#intrare :suma x , rata y, perioada de timp in luni
#output 

def sumafin(sum, dob, per):
    rat=dob/(100*12)
    R=sum*(rat*pow(1+rat,per)/(pow(1+rat,per)-1))
    return R*per
    
x=sumafin(1000,2,360)
print(x)

"""

#recursiv



