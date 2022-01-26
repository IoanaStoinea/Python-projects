"""""
Avem doua numere number1 si number2 intregi pe care le citim de la tastatura. 
Il avem si pe i ca si index care este initializat cu 0. Cat timp i este mai mic ca 5 se va face urmatoare operatiune number1 = nmber1-number2 si se 
va afisa valoarea lui number1 la fiecare pas. Indexul se va incrementa la fiecare pas.
"""""

print('Enter number1:')
number1=input()
print('Enter number2:')
number2=input()
i=0
while i<5:
    number1 = int(number1) - int(number2)
    print("Nummber1 = ", number1)
    i+=1 #i = i+1

