#----------------------------------------------
#            Eccezioni da alzare 
#----------------------------------------------
class ExamException(Exception):

        pass

#-----------------------------------------------
#   classe per leggere e convertire un file
#-----------------------------------------------

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


        #inizializzo la lista "data" per salvare i dati in formato numerico
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
                    elements[0]=None
                    continue

                #provo a convertire la temperatura in valore numerico
                try:
                    elements[1]=float(elements[1])
                #se non riesco gli assegno None e coninuo fino alla fine della lista
                except:
                    elements[1]=None
                    continue

                #aggiungo alla lista i nuovi valori convertiti
                data.append(elements)
            
        #chiudo il file
        my_file.close()

        return data

#-------------------------------------------------------------------------
#     Funzione controlla se i giorni sono ordinati e senza ripetizioni
#-------------------------------------------------------------------------
def check_list(time_series):

    for i in range(len(time_series)-1):
        #se "time_stamp" è maggiore o uguale a quello successivo 
        if(time_series[i][0]>=time_series[i+1][0]):
            #alzo eccezione
            raise ExamException('time_stamp ripetuti o non ordinati')

        

    return time_series


#--------------------------
#     corpo principale
#--------------------------
    
#------------------------------------------------
#     Funzione calcolo escursione giornaliera
#------------------------------------------------
def compute_daily_max_difference(time_series):

    #verifico se ci sono ripetizioni in un giorno
    time_series=check_list(time_series)
    #istanzio la lista dove memorizzo le escursioni termiche
    temperature_range=[]
    #variabile che memorizza l'indice della lista
    i_day=0

    
    for i in range(len(time_series)):

        #se è l'inizio dell'iterazione
        if i==0:
            #assegno minimo e massimo il primo elemento della lista
            min=time_series[0][1]
            max=time_series[0][1]
        #altrimenti      
        else:
            #confronto se il nuovo elemento è più piccolo di "min"
            if(min>time_series[i-1][1]):
                #lo riassegno a "min"
                min=time_series[i-1][1]

            #confronto per il valore massimo
            elif(max<time_series[i-1][1]):
                max=time_series[i-1][1]

            
        #calcolo il giorno alla mezzanotte precisa
        day_start_epoch=(time_series[i_day][0])-((time_series[i_day][0])%86400)
        
        #verifico quando cambia il giorno
        #se epoch attuale sottratto all'inizio del giorno supera i secondi fdi un giorno intero
        if(time_series[i][0]-day_start_epoch>=86400 or i==(len(time_series))-1):
            
            #assegno a index l'indice della lista in cui cambia giorno
            i_day=i
            #calcolo l'escursione termica 
            difference=max-min
            
            #se "min" e "max" coincidono 
            if(difference==0):
                temperature_range.append(None)
            else:
                temperature_range.append(round(difference,2))


            #riassegno "min" e "max" ai primi valori del giorno 
            min=time_series[i][1]
            max=time_series[i][1]
            
            
    return temperature_range
            
            
                
   

        




time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
temperature_range=compute_daily_max_difference(time_series)

print(time_series)

print('========================================')
print('Escursioni termiche gironaliere')

for i in range(len(temperature_range)):
    print('giorno_{} , {}'.format(i+1,temperature_range[i]))


