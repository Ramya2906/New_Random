from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    if(request.form['d'].lower()=="yes"):
        data4='1'
    else:
        data4='0'
    data5 = request.form['e']
    data6 = request.form['f']
    if(request.form['g'].lower()=="yes"):
        data7='1'
    else:
        data7='0'
    if(request.form['h'].lower()=="yes"):
        data8='1'
    else:
        data8='0'
    if(request.form['i'].lower()=="yes"):
        data9='1'
    else:
        data9='0'
    if(request.form['j'].lower()=="yes"):
        data10='1'
    else:
        data10='0'
    if(request.form['k'].lower()=="yes"):
        data11='1'
    else:
        data11='0'
        
    data12= request.form['l']
    data13= request.form['m']


    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)















