#classe per eccezioni esame
class ExamException(Exception):

        pass



# creo la classe per file CSV
class CSVTimeSeriesFile:

    def __init__(self,name):

        # nome del file 
        self.name=name


    def get_data(self):

        #verifico se riesco ad aprire e leggere il file
        try:
            my_file=open(self.name,'r')
            my_file.readline()
            print('ok')
        # se non riesco alzo un'eccezione
        except ExamException as e:
            print('Errore! File non aperto o illeggibile: "{}"'.format(e))

        #inizializzo una lista dove salvare i dati del file
        data=[]

        #apro il file
        my_file=open(self.name,'r')

        #leggo ogni riga del file
        for line in my_file:

            #faccio lo split sulla virgola 
            elements=line.split(',')

            if elements[0]!= 'epoch':

                data.append(elements)
                


        #chiudo il file
        my_file.close()

        return data
                    

        

    
            
            







            
#---------------------------------------------------
#          Corpo del programma
#---------------------------------------------------
time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()
print(time_series)