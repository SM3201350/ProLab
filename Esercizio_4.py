class CSVfile():

    def __init__(self,name):

        self.name = name

    def __str__(self):

        return 'CSVfile "{}".'.format(self.name)

    def get_data(self):

        values = []

        the_file = open(self.name,'r')
        
        for line in the_file:

            #faccio lo split di ogni riga sulla virgola
            elements = line.split(',')

            #se NON sto processando l'intestazione...
            if elements[0] != 'Date':

                #aggiungo alla lista dei valori questo valore
                values.append(elements)

        print(values)
        the_file.close()





my_file = CSVfile('shampoo_sales.csv')
print (my_file)
my_file.get_data()