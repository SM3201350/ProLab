#  Eccezioni da alzare in caso ci fossero problemi
class ExamException(Exception):

        pass



#--------------------------------
#        classe principale
#--------------------------------

class CSVTimeSeriesFile :

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


#------------------------------------------------
#              Funzione
#------------------------------------------------
def compute_daily_max_difference(time_series):

    #istanzio la lista dove memorizzo le escursioni termiche
    temperature_range=[]
    #istanzio una variabile che conta i giorni
    giorno=1
    #variabile che memorizza l'indice della lista
    index=0
    

    #itero 
    for i in range(len(time_series)):

        if i==0:
            min=time_series[0][1]
            max=time_series[0][1]
                
        else:
            if(min>time_series[i][1]):
                min=time_series[i][1]

            elif(max<time_series[i][1]):
                max=time_series[i][1]

                
        #calcolo il giorno alla mezzanotte precisa
        day_start_epoch=(time_series[index][0])-((time_series[index][0])%86400)
        
        #verificp quando cambia il giorno
        #se epoch attuale sottratto all'inizio del giorno supera i secondi fdi un giorno intero
        if(time_series[i][0]-day_start_epoch>=86400):
            #cambia il giorno
            giorno+=1
            
            #assegno a index l'indice della lista in cui cambia giorno
            index=i
            difference=max-min
            min=time_series[i][1]
            max=time_series[i][1]
            if(difference==0):
                temperature_range.append(None)
            else:
                temperature_range.append(difference)
            
            

    return temperature_range
            
            
                
   

        
#--------------------------
#     corpo principale
#--------------------------


time_series_file=CSVTimeSeriesFile (name='data.csv')
time_series=time_series_file.get_data()
prova=compute_daily_max_difference(time_series)
for i,value in enumerate(prova):
    print('giorno_{} = {}'.format(i,value))








