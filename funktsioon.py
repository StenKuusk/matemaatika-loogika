#1. Inside the function
#Loo funktsioon func().
#Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, prinditakse konsooli I´m inside the function
def func():
    print("I'm inside the function")
#2. My name is ...
#Loo funktsioon my_name_is(name).
#Funktsiooni sisendiks on string, mallis on muutuja nimeks name.
#Kirjutada funktsiooni "sisemus" nii, et igakord kui funktsiooni välja kutsuda, prinditakse konsooli My name is [name], kus [name] asemel prinditakse functiooni sisendiks antud nimi. Näiteks kui kutsutakse välja funtiooni my_name_is("Mari"), prinditakse konsooli My name is Mari
def my_name_is(name: str):
    print(f"My name is:{name}")
#3. Sum six
#Loo funktsioon sum_six(num).
#Funktsiooni sisendiks on int
#Funktsioon peab tagastama(return) number 6 ja funktiooni sisendi summa
#Näited:
#print(sum_six(1) # --> 7
#print(sum_six(6) # --> 12
def sum_six(num: int):
    return (num + 6)
#4. Sum numbers
#Loo funktsioon sum_numbers().
#Funktsiooni sisendiks on kaks täisarvu int, need võib tähistada näiteks a ja b. Mitme funktsiooni sisendu puhul eraldatakse need sulgude sees komaga. Nt: func(a, b)
#Funktsioon peab tagastama(return) sisendite summa.
#Näited:
#print(sum_numbers(5, 5) # --> 10
#print(sum_numbers(0, 25) # --> 25
def sum_numbers(a: int, b: int):
    return a + b
#5. USD to EUR
#Loo funktsioon usd_to_eur().
#Funktsiooni sisendiks on täisarv int
#Kirjuta funktsioon nii, et kui sisendiks on rahasumma dollarites, tagastab funktsioon summa eurodes. Funktsooni testimiseks oletame, et antud hetkel on kurss 1USD = 0.8EUR. Näited:
#print(usd_to_eur(100) # --> 80
def usd_to_eur(eur: int):
    return eur * 0,8