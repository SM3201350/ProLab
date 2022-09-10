#Manipolazione di liste e testing

#--------------------------------
#Funzione che verifica se una lista è vuota
#--------------------------------

def Full_List(list):

    if not list:
        return False
    else:
        return True


#--------------------------------
#Creo una funzione  che stampa una lista
#--------------------------------

def Stamp_List(list):

    #Verifico se la lista è vuota
    if Full_List(list) is True:

        #itero la lista e stampo ogni elemento
        for element in list:
            print('{}'.format(element))

    #Se la lista è vuota...
    else:
        print('ERRORE!! Impossibile stampare...Lista vuota')
        

    



#--------------------------------
#funzione che verifica gli elementi della lista se sono interi 
#--------------------------------

def Int_List(list):

    if Full_List(list) is True:
        for element in list:
            
            if type(element) != int:
                print('ERRORE!! Questo elemento in {} non è intero, ed è di questo tipo: {}'.format(list,type(element)))
                return False

        Stamp_List(list)
        return  True
    else:
        print('Impossibile stampare: Lista vuota')
        return None



#--------------------------------
#funzione che calcoli e stampi stat di una lista 
#--------------------------------

def Stat_List(list):

    if Int_List(list) is True:
        print('Stat lista:')
        print('Somma: {}'.format(sum(list)))
        print('Media: {}'.format(sum(list)/len(list)))
        print('Minimo: {}'.format(min(list)))
        print('Massimo: {}'.format(max(list)))

    else:
        print('ERRORE modificare la lista e riprovare')


    return False

    

#--------------------------------
#funzione che calcoli e stampi stat di una lista 
#--------------------------------

def Sum_Vect(list_1,list_2):

    #Verifico se le liste son di numeri interi
    if Int_List(list_1) & Int_List(list_2):


        #Inizializzo la lista finale
        end_list = []
        #Verifico se hanno la stessa dimensione
        if len(list_1) == len(list_2):

            for i in range(len(list_1)):
                end_list.append(list_1[i]+list_2[i])
                
            return end_list

        else:
            print('ERRORE!! Le liste non hanno la stessa dimensione')
            return end_list
            


    
first_list = [1,2,3,4]
second_list = [9,8,7,6]

print(Sum_Vect(first_list,second_list))
