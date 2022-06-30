from flask import Flask,jsonify,request
#from unicodedata import name
import numpy as np
#import traceback
#from flask import Flask,jsonify,request,redirect, url_for, render_template
import pickle




# import pandas as pd
# from pandas.core.reshape.merge import merge
# # import os, math
# import numpy as np
# from keras.models import load_model
# from keras.models import Sequential
# from keras.layers import Dense, Dropout, LSTM, Input, BatchNormalization
#import pickle

#pickled_model = pickle.load(open('prediction_of_glucose_level.pkl', 'rb'))
#prediction = pickled_model.predict([[[2.66288952e-01, 5.82982813e-08, 2.33161723e-01]],])

app = Flask(__name__)
@app.route("/", methods=['post'])
def hello():
    return "heysss"

@app.route('/Mypredict', methods=['POST'])
def Mypredict():
    print("a")
    ir=pickle.load(open('prediction_of_glucose_level2.pkl', 'rb'))
    if ir :
        try:
            print("b")
            json=request.get_json()
            print("c")
            temp=list(json[0].values())
            vals=np.array(temp).reshape((1,-1))
            vals = vals.reshape(vals.shape[0], 1, vals.shape[1])
            prediction=ir.predict(vals)
            return jsonify({'prediction': str(prediction[0])})
        except:
            return jsonify({'prediction': str(prediction[0])})
    else:
        return ('No model here to use')    

if __name__ == '__main__':
    app.run(threaded=False)
    #app.run(debug=True)    