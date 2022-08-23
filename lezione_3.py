#Apro, stampo e chiudo un file 
my_file = open('shampoo_sales.csv', 'r')
print(my_file.read())
my_file.close()
#
#
#
#Uso lo slicing:
my_file = open('shampoo_sales.csv', 'r')

my_file_contents = my_file.read()

if len(my_file_contents) >50:
    print(my_file_contents[0:50] + '...')
else:
    print(my_file_contents)

my_file.close()
#
#
#
#Leggo riga per riga
my_file = open('shampoo_sales.csv', 'r')

print(my_file.readline())

print(my_file.readline())

print(my_file.readline())

my_file.close()
#
#
#
#Riga per riga in modo pythonico
my_file = open('shampoo_sales.csv', 'r')

for line in my_file:
    print(line)
    
my_file.close()
#
#
#
#Slittare
mia_stringa = 'Ciao,come stai?'
lista_elementi = mia_stringa.split(',')
print (mia_stringa)
#
#
#
#Da stringa a floating point
mia_stringa = '5.5'

mio_numero = float(mia_stringa)

print('la stringa:{} e il doppio: {}'.format(mia_stringa,mio_numero*2))
#
#
#
#Aggiungere un elemento della lista
my_list = [1,2,3]

my_list.append(4)

for item in my_list:
    print(item)
#
#
#
#Leggere i valori di un file CSV
#inizializzo una lista vuota per salvare i valori
values = []

#apro e leggo il file, linea per linea
my_file = open('shampoo_sales.csv', 'r')
for line in my_file:

    #faccio lo split di ogni riga sulla virgola
    elements = line.split(',')

    #se NON sto processando l'intestazione...
    if elements[0] != 'Date':

        #setto la data e il valore
        date = elements[0]
        value = elements[1]

        #aggiungo alla lista dei valori questo valore
        values.append(value)

print(values)
my_file.close()
        
