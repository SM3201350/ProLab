class CSVFile:

    def __init__(self,name):

        self.name = name
        self.open_file = True

        if type((self.name)) == str:
            try:
            
                my_file = open(self.name,'r')
                my_file.readline()
            
            except Exception as e:
            
                self.open_file = False
                print('Errore di lettura file: "{}"'.format(e))

        else:
            raise Exception('Errore di scrittura file, non è una stringa')



    
    def get_data(self):
        if not self.open_file:
            
            print('Errore, file non aperto o illeggibile')
            return None

        else:
            
            data = []
            my_file = open(self.name,'r')
            
            

            
            for line in my_file:

                elements = line.split(',')
                elements[-1] = elements[-1].strip()

                if elements[0] != 'Date':
                    data.append(elements)

            my_file.close()

            return data



file = CSVFile('shampoo_sales.csv')
file.get_data()
        

 
        