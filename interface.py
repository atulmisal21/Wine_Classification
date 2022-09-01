from flask import Flask, jsonify,redirect,request
import config

from wine_classification.utils import WineClassification
# from wine_classification.utils import WineClassification.get_predicted_class
app = Flask(__name__)




@app.route('/')
def hello_flask():
    print('*'*90)
    print("We are testing Flask")
    print('*'*90)
    return jsonify({"Message" : "Welcome to Flask"})









##############################################################################
######################## Prediction ##########################################
##############################################################################
@app.route('/prediction1',methods = ['POST','GET'])
def prediction():

    input_data = request.form
    Alcohol = float(input_data['Alcohol'])
    Malic_acid = float(input_data['Malic_acid'])
    Ash = float(input_data['Ash'])
    Acl = float(input_data['Acl'])
    
    Mg = float(input_data['Mg'])
    Phenols = float(input_data['Phenols'])
    Flavanoids = float(input_data['Flavanoids'])
    Nonflavanoid_phenols = float(input_data['Nonflavanoid_phenols'])
    
    Proanth = float(input_data['Proanth'])
    Color_int = float(input_data['Color_int'])
    Hue = float(input_data['Hue'])
    OD = float(input_data['OD'])
    Proline = float(input_data['Proline'])


    Obj = WineClassification(Alcohol, Malic_acid, Ash, Acl,Mg,Phenols,Flavanoids,Nonflavanoid_phenols,Proanth,Color_int,Hue,OD,Proline)
    result = Obj.get_predicted_class()
    print("Predicted CLass is :",result)

    return jsonify({"Result":f"Predicted Class is : {result}"})


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug=False)