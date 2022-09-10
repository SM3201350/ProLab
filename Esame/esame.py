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
            print('Errore in apertura del file: "{}"'.format(e))
            


time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series=time_series_file.get_data()