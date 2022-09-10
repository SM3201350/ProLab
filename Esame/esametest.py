#classe per eccezioni esame
class ExamException(Exception):
    pass

#-------------------------------------
#          Classe che legge file
#-------------------------------------   
# creo la classe per file CSV
class CSVFile:

    def __init__(self,name):

        # nome del file 
        self.name=name

        
    def get_data(self):

      



        data=[]+[]

            #apro il file
            my_file = open(self.name,'r')

            #leggo ogni riga del file
            for line in my_file:

            
                #faccio lo split sulla virgola 
                elements=line.split(',')
                #sistemo la lista per stamparlo in modo più ordinato
                elements[-1]=elements[-1].strip()
            

                #converto gli elementi in valori numerici,saltando la prima 
                if elements[0]!= 'epoch':

                    #se sono presenti elementi non convertibili
                    try:
                        (elements[0])=int(elements[0])
                        (elements[1])=float(elements[1])

                    except ExamException:
                        elements[1]=0
                        continue

                
                    data.append(elements)
                
                
                
        
            #chiudo il file
            my_file.close()

            return data



            
#---------------------------------------------------
#          Corpo del programma
#---------------------------------------------------
time_series_file=CSVFile(name='data.csv')
time_series=time_series_file.get_data()
print(time_series[0:5])



