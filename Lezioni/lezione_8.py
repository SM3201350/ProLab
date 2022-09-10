class Model():
    
    def fit(slef,data):
        #fit non implementato nella classe base
        pass

    def predict(self,data):
        #predict non implementato nella classe base
        pass



class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

        
    def increment(self,data):

        prev_item = None
        increment = 0

        for item in data:
                
            if prev_item is not None:
                increment += item - prev_item
                
            prev_item=item

        media_increment=increment/(len(data)-1)

        return media_increment


    def predict(self,predict_data):

        incremento_medio=self.increment(predict_data)

        return predict_data[-1] + incremento_medio






class FitIncrementModel(IncrementModel):

    def __str__(self):
        return 'FitIncrementModel'
           
    def fit(self,fit_data):

        self.global_avg_increment=self.increment(fit_data)



    def predict(self,predict_data):

        parent_prediction = super().predict(predict_data)

        parent_predict_increment = parent_prediction - predict_data[-1]

        prediction_increment = (self.global_avg_increment + parent_predict_increment)/2

        prediction = predict_data[-1] + prediction_increment

        return prediction




test_fit_data = [8,19,31,41]
test_predict_data = [50,52,60]

# Test rapido su IncrementModel (non unit test in questo caso)
increment_model = IncrementModel()
fit_increment_model=FitIncrementModel()
prediction = increment_model.predict(test_predict_data) 
if prediction == 65:
    print('Test passato')
else: 
    raise Error('Errore, predizione non aspettata')

print(fit_increment_model.fit(test_fit_data))

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3,
                 
                 
                 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]





    
        

                



