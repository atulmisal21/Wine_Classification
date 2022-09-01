from operator import ge
import os 
print(os.getcwd())
print(os.listdir())
from wine_classification.utils import WineClassification

Obj = WineClassification(1,0.1778,0.433155,0.175258,0.293478,0.627586,0.556962,0.301887,0.495268,0.334471,0.487805,0.578755,0.547076)
result = Obj.get_predicted_class()
print("*"*60)
print("Predicted CLass is :",result)