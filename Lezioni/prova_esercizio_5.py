class CSVFile():

    def __init__(self,name):
        self.name = name
        self.read_file = True

        try:
            file = open(self.name,'r')
            file.readline()

        except Exception as e:
            self.read_file = False
            print('Errore! Impossibile aprire il file')


    def get_data(self):

        if self.read_file == False:
            print('Errore, file non aperto o illeggibile')

        else:
            values = []
            file = open(self.name, 'r')

            for line in file:
                elements = line.split(',')

                if elements[0] != 'Date':

                    values.append(elements)
            

            print(values)
            file.close()

            return values




class NumericalCSVFile(CSVFile):

    def get_data(self):
        
        string_data = super().get_data()
        numerical_value = []

        for line in string_data:

            numerical_line = []

            for i,element in enumerate(line):

                if i == 0:

                    numerical_line.append(element)
                    

                else:
                    try:
                        numerical_line.append(float(element))

                    except Exception as e:
                        print('Errore di conversione del valore "{}" in numerico: "{}"'.format(element,e))
                        
                    break

            if len(numerical_line) == len(line):
                numerical_value.append(numerical_line)

        return numerical_value

    
                    
                



data = NumericalCSVFile(name = 'shampoo_sales.csv')
data.get_data()

            

        

                

