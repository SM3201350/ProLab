#  Eccezioni da alzare in caso ci fossero problemi
class ExamException(Exception):

        pass



#--------------------------------
#        classe principale
#--------------------------------

class CSVFile:

    def __init__(self,name):

        #setto il nome del file
        self.name=name

    def get_data(self):

        #provo ad aprire il file
        try:
            my_file = open(self.name,'r')
        #alzo eccezione se non riesco
        except Exception as e:
            raise ExamException('Errore! File non leggibile: {}'.format(e))


        #inizializzo la lista data per salvare i dati in formato numerico
        data=[]

        #apro il file
        my_file = open(self.name,'r')

        #leggo ogni riga el file
        for line in my_file:

            #faccio lo split sulla virgola
            elements=line.split(',')
            #sistemo la lista pulendola alla fine
            elements[-1]=elements[-1].strip()

            #se non è l'intestazione
            if elements[0]!= 'epoch':

                #provo a convertire epoch in valore numerico
                try:
                    elements[0]=int(elements[0])
                #se non riesco gli assegno None e coninuo fino alla fine della lista
                except:
                    elements[0]=0
                    continue

                #provo a convertire la temperatura in valore numerico
                try:
                    elements[1]=float(elements[1])
                #se non riesco gli assegno None e coninuo fino alla fine della lista
                except:
                    elements[1]=0
                    continue

                #aggiungo alla lista i nuovi valori convertiti
                data.append(elements)
            
        #chiudo il file
        my_file.close()

        return data

        



#--------------------------
#     corpo principale
#--------------------------


time_series_file=CSVFile(name='data.csv')
time_series=time_series_file.get_data()
print((time_series[0][0]))


#test 
cambio_giorno=time_series[0][0]
time = time_series
for i in range(len(time_series)):
    #verificare quando cambia il giorno
    if(time_series[i][0]-cambio_giorno>=86400):
        cambio_giorno=time_series[i][0]
        print('{} giorno cambiato '.format(i))


   

        
        
    
