import numpy as np
import pickle

file_path = r'model.pkl'


class WineClassification():
    def __init__(self,Alcohol, Malic_acid, Ash, Acl,Mg,Phenols,Flavanoids,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline):
        self.Alcohol = Alcohol
        self.Malic_acid = Malic_acid
        self.Ash = Ash
        self.Acl = Acl
        self.Mg = Mg
        self.Phenols = Phenols
        self.Flavanoids = Flavanoids
        self.Nonflavanoid_phenols = Nonflavanoid_phenols
        self.Proanth = Proanth
        self.Color_int = Color_int
        self.Hue = Hue
        self.OD = OD
        self.Proline = Proline
        

    def get_model(self):
        with open( 'model.pkl','rb') as f:
            self.model = pickle.load(f)
    
    
    
    def get_predicted_class(self):
        self.get_model()
        input_array = np.array([self.Alcohol,self.Malic_acid,
                                self.Ash,self.Acl,self.Mg,self.Phenols,self.Flavanoids,self.Nonflavanoid_phenols,self.Proanth,self.Color_int,self.Hue,self.OD,self.Proline],ndmin = 2)
        print(input_array)
        
        predicted_class = self.model.predict(input_array)[0]
        
        classes = { 1 : "White", 
                    2 : "Red",
                    3: "Rose" }

        result = classes[predicted_class]
        return result

if __name__ == "__main__":
    Obj = WineClassification(1,0.1778,0.433155,0.175258,0.293478,0.627586,0.556962,0.301887,0.495268,0.334471,0.487805,0.578755,0.547076)
    result = Obj.get_predicted_class()
    print("*"*60)
    print("Predicted CLass is :",result)
