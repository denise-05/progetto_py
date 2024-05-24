fruits=["orange","lemon","banana","kiwi"]   #rimuovere banana dall'elenco 
fruits.remove("banana")                      
fruits

print(fruits[-1])   #indicizzazione negativa per stampare l'ultimo elemento

a=50
b=10
if a==b:
    print("yes")   #stampa si se a e b sono uguali altrimenti stampa no
else:
    print("no")    

a=50
b=10
if a==b:
    print("1")   #stampa 1 se a è euguale a b
elif a>b:
    print("2")   #stampa 2 se a è maggiore di b
else:
    print("3")   #altrimenti stampa 3

c=30
d=70
if a==b and c==d:
    print("hello")     #stampa hello se a è uguale a b E se c è uguale a d

 if a==b or c==d:
    print("hello")     #stampa hello se a è uguale a b O se c è uguale a d 

i=1
while i<6:
    print(i)         #ciclo while 
    i+=1             #stampa finchè arriva a 6

i=1
while i<6:
    if i==3:
        break     #arresta il ciclo se i è uguale a 3
    i+=1      

for x in fruits:
    if x=="banana":
        continue       #quando arriva a banana continua con l'elemento successivo
    print(x)

def my_funcion():
    print("hello from a function")  #creare una funzione denominata my_function

my_funcion()               #per eseguirla 

def my_function_2(x):
    return x+5            

class myclass:       #creacre una classe denominata myclass
    x=5
p1=myclass()    #creare un oggetto di myclass chiamato p1
print(p1.x)     #utilizzare l'oggetto p1 per stampare il valore di x   

car= {
    "brand":"ford",
    "model":"mustang",    #creazione di un dizionario
    "year":"1964"}
car
print(car.get("model"))   #stampa il valore della chiave model del dizionario

car["year"]=2020  #sostituisce 1964 con 2020
car["color"]="red"#aggiunge la coppia di chiave valore al dizionario
car.pop("model")  #rimuove modello dal dizionario
car
car.clear() #per svuotarlo 
