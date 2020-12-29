from flask import Flask, jsonify
import dati

app = Flask(__name__)

app.config['JSON_AS_ASCII']=False #Latviešu burtiem

@app.route('/')
def index():
  print(dati.vielas)
  return "Labrīt!"

@app.route('/api/v1/vielas')
def vielas():
  return jsonify(dati.vielas)

@app.route('/api/v1/viela/<vielasID>')
def viela(vielasID):
  viela=f"Viela ar doto ID {vielasID} nav atrasta!"
  for v in dati.vielas:
    if v['id']==int(vielasID):
      viela=str(v)
  
    return jsonify(viela)
  
    

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
