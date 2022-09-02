class Model():

    def fit(self, data):
        pass
    
    def predict(self, data):
        pass


class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

    def compute_avg_increment(self, data):
        # Variabile di supporto per il valore precedente
        prev_item = None

        # Preparo una variabile di supporto per calcolare l'incremento medio
        increments = 0
        
        # Processo i mesi in input su cui fare la predizione
        for item in data:

            # Caloclo l'incremento ma non se son o al primo
            # giro ovvero se non e' definito il "prev_item"
            if prev_item is not None:
                increments += item - prev_item

            # Assegno questo valore come precedente
            prev_item = item

        # Calcolo l'incremento medio divivendo la somam degli incrmenti sul totale dei dati (meno uno)
        avg_increment = increments / (len(data)-1)
        
        return avg_increment

    def predict(self, predict_data):
        
        #Calcolo l'incremento medio sui dati della predict
        avg_increment = self.compute_avg_increment(predict_data)

        # Torno la predizione (incremento medio sommato all'ultimo valore)
        return predict_data[-1] + avg_increment



test_predict_data = [50,52,60]


prediction = IncrementModel().predict(test_predict_data)
print('{}'.format(prediction))