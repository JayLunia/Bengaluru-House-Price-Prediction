from flask import Flask , render_template,request , jsonify
import pandas as pd
import pickle
app = Flask(__name__)

data=pd.read_csv('final_data.csv')

model= pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def index():
    locations=sorted(data['location'].unique())
    print(locations)
    return render_template('index.html',title='House Price Predictor',locations=locations)

@app.route("/pred",methods=['POST'])
def pred():
    if request.method == 'POST':
        loc=request.form.get('loc')
        bhk=request.form.get('bhk')
        br=request.form.get('br')
        tsf=request.form.get('tsf')
        input=pd.DataFrame([[loc,bhk,tsf,br]],columns=['location','bhk','total_sqft','bath'])
        output=round(model.predict(input)[0] * 100000,2)
        return jsonify(output)


if __name__=="__main__":
    app.run(debug=True)
# D:\flask api\sms spam\__pycache__