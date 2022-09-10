    def get_data(self):

        self.file_ok=1
        #verifico se riesco ad aprire e leggere il file
       
            

        if self.file_ok==0:
            print('Errore di apertura file')

        else:
            #inizializzo una lista dove salvare i dati del file
            data=[]+[]

            #apro il file
            my_file=open(self.name,'r')

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
time_series_file=CSVFile('daa.csv')
time_series=time_series_file.get_data()