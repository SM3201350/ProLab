#==============================
#  Classe per file CSV
#==============================

class CSVFile:

    def __init__(self, name):
        
        # Setto il nome del file
        self.name = name
        
        
    def get_data(self):

        try:
            my_file=open(self.name,'r')
            my_file.readline()
        except Exception:
            print('Mona')


csv_file=CSVFile('shampo_sales.csv')
file=csv_file.get_data()