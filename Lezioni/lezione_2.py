# iterare e stampare una lista 
number_list = [32,12,45,-4,5,4,123,17]

for item in number_list:
    if item < 5:
        print (item)


# accedere ai dizionari
my_dict = {'Trieste': 34100, 'Padova': 35100}
my_dict = {'Trieste': 'TS', 'Padova' : 'PD'}

print ('CAP di Trieste: {}' .format(my_dict['Trieste']))


#ESERCIZIO scrivere una funzione che sommi gli elementi della lista
def sum_list(list):
    result = 0
    for item in my_list:
        result = result + item
    print (result)


my_list = [1,2,3,4,5,6,7,8,9,-49.35]
sum_list(my_list)


