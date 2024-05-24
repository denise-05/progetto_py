print("hello wolrd") #genera hello world

if 5>2:
    print("yes") #stampa si se 5 è maggiore di 2 

x=5
y=10
print(x+y) 
z=x+y
print(z)      #somma tra due variabili

def myfunc():
    global x       #per far si che la variabile x appartenga all'ambito globale 
    x="fantastic"

x=5
print(type(x))  

x="hello world"
print(type(x))

x=[1,2,3]
print(type(x))

x=(1,2,3)                  #conoscere il tipo di variabile
print(type(x))

x=True
print(type(x))

x=5
x=complex(x)              #coverire una variabile 
x

x=5
x=float(5)
x

x="hello world"
print(len(x))          #lunghezza di una stringa

txt="hello world"
x=txt[0]            #primo carattere della stringa    
x

txt="hello world"
x=txt[2:5]            #caratteri dall'indice due all'indice 4    
x

txt="hello world"
x=txt.strip()           #restituisce la stinga senza spazi vuoti all'inizio o alla fine 
x

txt="hello world"
x=txt.upper()           #converte il carattere in maiuscolo 
x

txt="hello world"
x=txt.lower()           #converte il carattere in minuscolo
x

fruits=["apple","banana"]
if "apple" in fruits:          #(in) operatore di appartenenza
    print("apple is a fruit")

print(fruits[1])              #stampa il secondo elemento dell'elenco

fruits[0]="orange"        #sostituisce mela con arancia 
fruits

fruits.insert(1,"lemon") #inserire limone come secondo elemento     
fruits

fruits.append("kiwi")   #aggiungere kiwi all'elenco    
fruits