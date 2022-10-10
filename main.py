# if __name__ == '__main__':
#     print_hi('PyCharm')
#Exercitiul 1
def cmmdc(a, b):
    if b == 0:
        return a
    else:
        return cmmdc(b, a % b)

k=0
def cmmdcM():
    global k
    k = int(input('Introduceti cate numere:'))
    numere = []

    for i in range(1, k+1):
        n = int(input('Introdu un numar'))
        numere.append(n)

    n1 = numere[0]
    numere.pop(0)

    for i in numere:
        n2 = i
        c = cmmdc(n1, n2)
        n1 = c

    print(c)


#cmmdcM()

#Exercitiul 2
def num_vocale(cuvant):
    nr_vocale = 0
    for c in cuvant:
        if c in "aeiouAEIOU":
            nr_vocale = nr_vocale+1
    return nr_vocale

#print(num_vocale('Afara'))

#Exercitiul 3
def occurence(str1, str2):
    return len(str2.split(str1))-1

#print(occurence('ala','ala bala portocal'))


#Exercitiul 4
def uppertolower(cuvant):
    for c in cuvant:
         if c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
             cuvant= cuvant.replace(c,'_'+c)
    cuvant=cuvant.lower()
    cuvant = cuvant[1:len(cuvant)]
    print(cuvant)


#uppertolower('AziELuni')

#Exercitiul 6
def palindrom(nr):
    aux=0
    copie=nr
    while nr!=0:
        c = nr%10
        nr = int(nr/10)
        aux = aux*10+c

    if copie==aux:
        print('Este palindrom')
    else:
        print('Nu este palindrom')


palindrom(11211)

#Exercitiul 7
def extractnumber(cuvant):
    numar=[]
    for i in range(0,len(cuvant)-1):
        if cuvant[i].isdigit()==True:
            break
    while cuvant[i].isdigit()==True:
        numar.append(cuvant[i])
        i=i+1
    print(numar)

extractnumber("An apple is 123 USD")






